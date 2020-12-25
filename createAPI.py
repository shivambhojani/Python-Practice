from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    c = a + b
    result = {
        "Number1": a,
        "Number2": b,
        "Answer": c
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
