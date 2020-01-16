import sqlite3
from secrets import token_urlsafe

from flask import Flask, jsonify, request

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("todo.db", isolation_level=None, check_same_thread=False)
conn.row_factory = dict_factory
cur = conn.cursor()


def load():
    cur.execute("SELECT * from todo")
    return cur.fetchall()


class Item:
    MEMBERS = ["title", "content", "author", "completed", "removevd", "project", "target", "private"]
    cid: str
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
        self.cid = token_urlsafe(5)
        self.title = title
        self.content = content
        self.author = author
        self.completed = False
        self.removed = False
        self.project = project
        self.target = target
        self.private = private

    @classmethod
    def fromid(cls, uid):
        cur.execute("SELECT * from todo where id=?", uid)
        qur = cls(**cur.fetchall()[0])
        qur.cid = uid
        return qur

    def editinfo(self, **kwargs):
        for member in self.MEMBERS:
            exec("self." + member + " = " + kwargs[member])

    @property
    def dict(self):
        return {
            'id': self.cid,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'completed': self.completed,
            'removed': self.removed,
            'project': self.project,
            'target': self.target,
            'private': self.private,
        }

    @property
    def tuple(self):
        return (
            self.cid,
            self.title,
            self.author,
            self.content,
            self.completed,
            self.removed,
            self.project,
            self.target,
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


@app.route('/<cid>', methods=['DELETE'])
def deletetodo(cid):
    cur.execute("DELETE FROM todo WHERE id=?", (cid,))
    return cid, 204


@app.route('/', methods=['PUT'])
def edittodo():
    req = request.get_json()
    todo = Item.fromid(req["id"])
    todo.editinfo(**req)
    cur.execute("UPDATE todo SET id=?,title=?,content=?,author=?,completed=?,removed=?,project=?,target=?,private=? "
                "WHERE id=?", todo.tuple + (todo.cid,))
    return req, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
