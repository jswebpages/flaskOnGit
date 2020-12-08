from flask import Flask, request, render_template
from random import randint, sample
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

app.config["SECRET_KEY"] = "pydata1"
debug = DebugToolbarExtension(app)


@app.route("/")
def home():
    """Showing home Page"""
    return render_template("home.html")

@app.route("/about")
def about():
    """Showing about Page"""
    return render_template("about.html")

@app.route("/lucky")
def lucky():
    """Showing lucky Page"""
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    #roll = int(dice1) + int(dice2)
    return render_template("lucky.html", Dice1 = dice1, Dice2 = dice2)

@app.route("/form")
def form():
    """Showing form Page"""
    return render_template("form.html")

@app.route("/greet")
def greet():
    """Showing greet Page"""
    username = request.args["username"]
    return render_template("greet.html",  username=username)

@app.route("/calc")
def calc():
    """Showing calc Page"""
    num1 = int(request.args["num1"])
    num2 = int(request.args["num2"])
    operations = request.args["options"]

    return render_template("calc.html", num1=num1, num2=num2, operations=operations)

@app.route("/madlibs")
def madlibs():
    """Showing madlibs Page"""
    return render_template("madlibs.html")

@app.route("/blog")
def blog():
    """Showing blogs Page"""
    return render_template("blog.html")

@app.route("/entercalc")
def entercalc():
    """test"""
    return render_template("entercalc.html")

@app.route("/story")
def story():
    """story"""

    animal = request.args["animal"]
    state = request.args["state"]
    snack = request.args["snack"]
    wear = request.args["wear"]
    petname = request.args["pet_name"]
    story = request.args["options"]

    return render_template("story.html", animal=animal,state=state,snack=snack,wear=wear,petname=petname, story=story)

