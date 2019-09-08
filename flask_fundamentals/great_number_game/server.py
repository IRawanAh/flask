from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)
app.secret_key ="hi"

@app.route('/',defaults={"right": 'none' ,"wrong": 'none'})
def index(right,wrong):
    session["number"]=random.randint(1, 100)
    print(session["number"])
    return render_template("index.html",right="none", wrong="none")

@app.route('/guess', methods=['POST'],defaults={'right': 'none' ,'wrong': 'none'})
def index2(right,wrong):
    info=request.form["answer"]
    if int(info)==session["number"]:
        right="right"
        text="Good Job!"
    else:
        wrong="wrong"
        right="none"
        if int(info)>session["number"]:
            text="Too High!"
        else:
            text="Too Low!"

       

    return render_template("index.html", right=right, wrong=wrong, text=text )



if __name__ == "__main__":
    app.run(debug=True)
