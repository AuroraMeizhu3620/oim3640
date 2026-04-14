from flask import Flask, render_template, request
from stocks import get_price

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/hello/<name>") # <> creates a parameter
def hello(name):
    if name is None:
        name = "World"
    name = name.capitalize()

    html = f"<h1 style='color:red;'>Hello, {name}!</h1> <p> Welcome to Flask development.</p>"
    return render_template("hello.html", name=name, html=html) # render_template looks for templates folder and hello.html file

@app.route('/square/<int:n>')
def square(n):
    result = n **2
    #return f"{n} squared is {n**2}"
    return render_template("square.html", n=n, square=result)

@app.route("/stocks/<ticker>")
def stock(ticker):
    price = get_price(ticker)
    return f"The current price of {ticker.upper()} is ${price:.2f}"

@app.get("/ticker")
def ticker():
    return render_template("stockform.html")

@app.post("/ticker")
def ticker_post():
    ticker = request.form.get("symbol")
    price = get_price(ticker)
    return f"The current price of {ticker.upper()} is ${price:.2f}"

if __name__ == "__main__":
    app.run(debug=True)

# 127.0.0.1 is only a local IP
# :5000 is called a port


