from flask import Flask, render_template, request

# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")


@app.route("/sum")
def sum_route():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


@app.route("/sub")
def sub_route():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


@app.route("/mul")
def mul_route():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
