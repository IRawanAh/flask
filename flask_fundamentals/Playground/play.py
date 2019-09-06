from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html", times=3, color="green")	# notice the 2 new named arguments!



@app.route('/play/<num>')
def index2(num):
    return render_template("index.html", times=int(num), color="green")	# notice the 2 new named arguments!


@app.route('/play/<num>/<color>')
def index3(num, color):
    return render_template("index.html", times=int(num), color=color)	# notice the 2 new named arguments!


if __name__=="__main__":
    app.run(debug=True)
