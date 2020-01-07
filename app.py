import json
from secrets import token_urlsafe

from flask import Flask, jsonify, request

app = Flask(__name__)


class Item:
    id: str
    title: str
    content: str
    author: str
    completed: bool
    removed: bool
    project: str
    target: str
    private: bool

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

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'project': self.project,
            'target': self.target,
            'completed': self.completed,
            'removed': self.removed,
            'private': self.private}


@app.route('/', methods=['GET'])
def todolist():
    with open('todo.json', 'r') as f:
        res = jsonify(json.load(f))
        res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res


@app.route('/', methods=['POST'])
def maketodo():
    todo = Item(**request.get_json())
    with open('todo.json', 'r') as f:
        todofile = json.load(f)
        todofile.append(todo.dict)
    with open("todo.json", "w") as f:
        json.dump(todofile, f)
    return todo.dict


@app.route('/', methods=['DELETE'])
def deletetodo():
    pass


@app.route('/', methods=['PUT'])
def edittodo():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
