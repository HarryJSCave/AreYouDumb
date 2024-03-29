import os
import pathlib
from urllib import response
import requests
from flask import Flask, abort, redirect, render_template, request, session
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from flask_mysqldb import MySQL
import user
import quiz

 
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
    # ngl just going to have to trust the api on this one
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
        audience = GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=10
    )
    session["google_id"] = id_info.get("sub") # massive int for users 
    session["name"] = id_info.get("name")     # nickname
    return redirect("/home")

# does what is says on the tin 
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
    newUser = user.User(session['google_id'], session['name'])
    newUser.addUserToDatabase()
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
        r = result.getResponse()
        return render_template('response.html', result = result, response = r)


@app.route('/leaderboard')
def leaderboard():
    # call database and create a model of leaderboard 
    leaderboard = user.Leaderboard() 
    length = min(20,(len(leaderboard.board.keys()))) 
    return render_template("Leaderboard.html", length = length, leaderboard = leaderboard)

@app.route('/stats')
def stats():
    userS = user.UserStats(session['google_id']) 
    return render_template("Stats.html", stats = userS)
    
if __name__ == '__main__': 
    app.run(debug=True)