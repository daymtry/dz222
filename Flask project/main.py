
from flask import Flask, render_template

import random


app = Flask(__name__)


max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza1=20)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza2=30)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza3=40)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza4=50)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza5=60)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza6=70)

@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", price_pizza7=80)


@app.get("/contacts/")
def contacts():
    context = {
        "first_number": random.randint(101, 999),
        "second_number": random.randint(1001, 9999)
    }
    return render_template("contacts.html", **context)


@app.get("/test/")
def test():
    context = {
        "max_score": max_score,
        "title": "Test Title",
        "test_name": test_name,
        "students": students
    }
    return render_template("test.html", price_pizza1=20)


if __name__ == "__main__":
    app.run()
