from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to my page</h1>"

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/home")
def homePage():
    return "<h1>Home is where the heart is, under maintenance, come back</h1>"

@app.route("/Exit")
def exitPage():
    return "<h1>See ya later, do visit</h1>"

if __name__ == "__main__":
    app.run()
