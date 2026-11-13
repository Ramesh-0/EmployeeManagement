from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management Portal"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "Employee Registered Successfully"

    return """
        <h2>Employee Registration</h2>
        <form method="POST">
            <input name="name" placeholder="Employee Name">
            <button type="submit">Register</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True)