from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)
app.secret_key ="hi"

@app.route('/')
def index():
    session["gold"]=0
    session["activities"]=""

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def index2():
    print(request.form["btnValue"])
    if request.form["btnValue"]=="farm":
        num=random.randint(10, 20)
        session["gold"]+=num
        session["activities"]+="Earned "+str(num)+ " from the farm!\n"

    if request.form["btnValue"]=="cave":
        num=random.randint(5, 10)
        session["gold"]+=num
        session["activities"]+="Earned "+str(num)+ " from the cave!\n"

    if request.form["btnValue"]=="house":
        num=random.randint(2, 5)
        session["gold"]+=num
        session["activities"]+="Earned "+str(num)+ " from the house!\n"

    if request.form["btnValue"]=="casino":
        num=random.randint(0, 50)
        session["gold"]-=num
        session["activities"]+="Earned a casino and lost "+str(num)+ " golds!\n"


    return render_template("index.html" )

if __name__ == "__main__":
    app.run(debug=True)
