from flask import blueprints, render_template, request

main= blueprints.Blueprint("main", __name__)

@main.route("/")
def inicio():
    return render_template("index.html")
    