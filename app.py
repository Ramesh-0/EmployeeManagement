from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management Portal"

@app.route("/search")
def search():
    name = request.args.get("name", "")

    return f"Searching for employee: {name}"

if __name__ == "__main__":
    app.run(debug=True)