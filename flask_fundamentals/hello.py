from flask import Flask 
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return 'Hello Worllllld!' 

@app.route('/s')
def success():
  return "success"
if __name__=="__main__":
    app.run(debug=True)   

