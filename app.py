import json
from secrets import token_urlsafe

from flask import Flask, Response

app = Flask(__name__)


class Item:
    id: str
    title: str
    content: str
    author: str
    completed: bool
    removed: bool
    private: bool
    project: str
    target: str

    def __init__(self, title: str, content: str, author: str, project: str = None, target: str = None,
                 private: bool = False):
        self.id = token_urlsafe(10)
        self.title = title
        self.content = content
        self.author = author
        self.project = project
        self.target = target
        self.completed = False
        self.removed = False
        self.private = private


@app.route('/', methods=['GET'])
def todolist():
    with open('todo.json', 'r') as f:
        res = Response(json.load(f))
        res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res


@app.route('/', methods=['POST'])
def maketodo():
    pass


@app.route('/', methods=['DELETE'])
def deletetodo():
    pass


@app.route('/', methods=['PUT'])
def edittodo():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
