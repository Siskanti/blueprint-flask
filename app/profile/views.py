from flask import Blueprint, render_template

profile_blueprint = Blueprint('profile', __name__)
@profile_blueprint.route("/")
def index():
    return "Ini dari profile"
