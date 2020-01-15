from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a secret"
csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit",methods=["POST"])
def sub():
    a = request.form.get('name')
    f = open("new.txt","a")
    f.write(a+"\n")
    f.close()
    return f"<h1>{a}</h1>"

if __name__ == "__main__":
    app.run(port=8000,debug=True)