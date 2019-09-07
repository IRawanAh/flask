from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)          


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def create_user():
    return render_template("result.html", info=request.form)

if __name__ == "__main__":
    app.run(debug=True)
