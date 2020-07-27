# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
# from helpers import get_score, GENRES_LIST

# FINAL - DO NOT TOUCH
#edit


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("website.html")
