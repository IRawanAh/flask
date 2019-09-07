from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="hi"

@app.route('/')
def index():
    session["count"]=1
    return render_template("index.html")

@app.route('/addvisit', methods=['POST'])
def index2():
    if 'count' in session:
        session['count'] =session['count']+1
        return render_template("index.html")
    return "not logged in"


@app.route('/destroy_session', methods=['POST'])
def index3():
    if 'count' in session:
       session["count"]=1
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
