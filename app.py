from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import belly_button


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/names')
def names():
    names_data = belly_button.names()
    return render_template("names.html", names_data=names_data)

# @app.route('/names')
# def names():
#     data = belly_button.names()
#     print(data)
#     return render_template("names.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
