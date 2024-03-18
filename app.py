from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello World"

@app.route("/about")
def about():
    return f"Página 'Sobre'"

if __name__ == "__main__":
    app.run(debug=True)