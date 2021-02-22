import datetime
import os

from flask import Flask, Response, request
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
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
    Todo(title="Simple todo A", text="1233458498").save()
    Todo(title="Simple todo B", text="5415464555").save()
    Todo.objects(title__contains="B").update(set__text="Hello World!")
    todos = Todo.objects().to_json()
    return Response(todos, mimetype="application/json", status=200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)