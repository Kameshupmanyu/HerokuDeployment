from flask import Flask , render_template , request ,redirect

import model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET','POST'])
def kam():
    if request.method == 'POST':
       model.emotion()
    return redirect('/') 


if __name__ == "__main__":
    app.run(debug=True,port=8000)