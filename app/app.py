from flask import Flask, redirect, url_for
from flask import render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "zxvqw"
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project-select.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else: 
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
        

# @app.route("/<project>")
# def project(project):
#     return f"Hello {project}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)

