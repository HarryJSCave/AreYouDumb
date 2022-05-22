from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html") 

@app.route('/Question/<cat>')
def question(cat):
    return render_template("Question.html", cat = cat)

@app.route('/Question/responce')
def responce():
    return render_template("Responce.html")
    
if __name__ == '__main__': 
    app.run(debug=True)