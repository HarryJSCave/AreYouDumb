from flask import Flask, abort, redirect, render_template, session
#import question,stats,user 

app = Flask(__name__)
app.secret_key = "beans"

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else: 
            return function()
    return wrapper 

@app.route('/login')
def login():
    session["google_id"] = "f"
    return redirect("/home")

@app.route('/callback')
def callback():
    pass

@app.route('/logout')
def logout():
    pass



@app.route('/')
def index():
    return "<a href='/login'><button> login </button></a>"

@app.route('/home')
def home():
    return render_template("Home.html") 

@app.route('/question/<category>')
@login_is_required
def question(category):
    return render_template("Question.html", cat = category)

@app.route('/question/responce')
def responce():
    return render_template("Responce.html")

@app.route('/leaderboard')
def leaderbord():
    return render_template("Leaderboard.html")

@app.route('/stats')
def stats():
    return render_template("Stats.html")
    
if __name__ == '__main__': 
    app.run(debug=True)