
from flask import Flask,render_template

from todo_app.flask_config import Config
from todo_app.data import session_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=session_items.get_items())
