import os
from quart import Quart, g, render_template, jsonify
from utils import connect_db

app = Quart(__name__)

from api import api
app.register_blueprint(api, '/api')

app.config.update({
    'DATABASE': os.path.join(app.root_path, 'arduino.db')
})

@app.cli.command()
def init_db():
    create_db()

def create_db():
    db = connect_db(app.config['DATABASE'])
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    return g.sqlite_db

@app.before_request
def set_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db(app.config['DATABASE'])

@app.route('/', methods=['GET'])
async def index():
    db = get_db()
    posts = (db.execute("SELECT * FROM posts;")).fetchall()
    return await render_template('index.html', posts=posts)