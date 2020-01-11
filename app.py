import sqlite3
from flask import Flask, jsonify, request
from secrets import token_urlsafe

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("todo.db", isolation_level=None)
conn.row_factory = dict_factory
cur = conn.cursor()


def load():
    cur.execute("SELECT * from todo")
    return cur.fetchall()


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
        self.id = token_urlsafe(5)
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
            'private': self.private,
        }

    @property
    def tuple(self):
        return (
            self.id,
            self.title,
            self.content,
            self.author,
            self.project,
            self.target,
            self.completed,
            self.removed,
            self.private,
        )


@app.route('/', methods=['GET'])
def todolist():
    res = jsonify(load())
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res


@app.route('/', methods=['POST'])
def maketodo():
    todo = Item(**request.get_json())
    cur.execute("INSERT INTO todo values (?,?,?,?,?,?,?,?,?)", todo.tuple)
    return todo.dict


@app.route('/', methods=['DELETE'])
def deletetodo():
    pass


@app.route('/', methods=['PUT'])
def edittodo():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
