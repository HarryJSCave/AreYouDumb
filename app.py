import os
import pathlib
import requests
from flask import Flask, abort, redirect, render_template, request, session
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
#import question,stats,user 

app = Flask(__name__)
app.secret_key = "beans"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "497353706817-b5sbmr45kftqqtts9puegi19kcohp8kp.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri= "http://127.0.0.1:5000/callback" )

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else: 
            return function()
    return wrapper 

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500) # state does not match
    
    credentials = flow.credentials 
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session = cached_session)
    id_info = id_token.verify_oauth2_token(
        id_token= credentials._id_token,
        request = token_request,
        audience = GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/home")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")



@app.route('/')
def index():
    return "<a href='/login'><button> login </button></a>"

@app.route('/home')
@login_is_required
def home():
    return render_template("Home.html") 

@app.route('/question/<category>')
def question(category):
    return render_template("Question.html", cat = category)

@app.route('/question/responce')
def responce():
    return render_template("Responce.html")

@app.route('/leaderboard')
def leaderboard():
    return render_template("Leaderboard.html")

@app.route('/stats')
def stats():
    return render_template("Stats.html")
    
if __name__ == '__main__': 
    app.run(debug=True)