from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") 

@app.route('/Question/<cat>')
def question(cat):
    return render_template("question.html", cat = cat)

@app.route('/Question/responce')
def responce():
    return render_template("responce.html")
    
if __name__ == '__main__': 
    app.run(debug=True)