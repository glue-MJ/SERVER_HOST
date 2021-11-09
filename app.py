from flask import Flask, render_template, url_for, request, redirect, sessions
import subprocess

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        if request.form["TRIGGER"] == "START PROGRAM":
            subprocess.run("python collector.py", shell=True)
            print("RUN")
        else:
            pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)