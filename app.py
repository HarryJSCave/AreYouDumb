import os
import pathlib
from unittest import result
import requests
from flask import Flask, abort, redirect, render_template, request, session
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import quiz 
from flask_mysqldb import MySQL
 
app = Flask(__name__)
app.secret_key = "beans"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dc_2060'
mysql = MySQL(app)

#Auth and Login 
####################################################################
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

    print("----------------------")
    print(id_info.get("email"))

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/home")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


################################################################################
#
# GamePlay 
################################################################################
@app.route('/')
def index():
    return render_template("login.html") 
    

@app.route('/home')
@login_is_required
def home():

    return render_template("Home.html") 

@app.route('/question/<category>', methods=['GET','POST'])
def askQuestion(category):
    # fetch question
    # #build question 
    
    question = quiz.Question(category) 
    if request.method == 'GET':
        if (question.alreadyAnswered()):
            return render_template("AlreadyCompleted.html", question = question)
        else:
            
            return render_template("Question.html", question = question)

            
    else:
        result = quiz.Result(question, request.form['answer'], request.form['timerForm']) 
        result.sendToDatabase()
        return render_template('response.html', result = result)


@app.route('/question/response')
def response(answer):
    # return postive or negative response
    return render_template("response.html")

@app.route('/leaderboard')
def leaderboard():
    # call database and create a model of leaderboard 
    return render_template("Leaderboard.html")

@app.route('/stats')
def stats():
    # call database a retrive user stats 
    return render_template("Stats.html")
    
if __name__ == '__main__': 
    app.run(debug=True)