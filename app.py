from flask import Flask

app = Flask(__name__)


class Item:
    author: str
    title: str
    content: str
    completed: bool
    removed: bool
    private: bool
    project: str
    target: str


@app.route('/', methods=['GET'])
def todolist():
    pass


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
