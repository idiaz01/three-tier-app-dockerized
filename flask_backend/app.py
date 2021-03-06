import datetime
import os

from flask import Flask, Response, request
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "*"}})

with open(os.environ['MONGODB_PASSWORD_FILE'], 'r') as pwd_file:
    mongodb_api_pwd = pwd_file.read()

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': mongodb_api_pwd,
    'db': 'application'
}

db = MongoEngine()
db.init_app(app)

class Todo(db.Document):
    title = db.StringField(max_length=60)
    text = db.StringField()
    done = db.BooleanField(default=False)
    pub_date = db.DateTimeField(default=datetime.datetime.now)


@app.route("/api")
def index():
    Todo.objects().delete()
    Todo(title="My first todo", text="Commit my changes").save()
    Todo(title="Another one", text="Go to the supermarket").save()
    todos = Todo.objects().to_json()
    return Response(todos, mimetype="application/json", status=200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)