from flask import Flask

app = Flask(__name__)
@app.route("/")
def welcom():
    return "Welcome to my page boss"

@app.route("/contact")
def contactPage():
    return "I know a guy who knows a guy, contact me ASAP"

@app.route("/home")
def homePage():
    return "Home is where the heart is, under maintenance, come back"
@app.route("/Exit")
def exitPage():
    return "See ya later, do visit"

if __name__ == "__main__":
    app.run()
