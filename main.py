#!/usr/bin/env python3

from flask import Flask, request
from visitors import Visitors


app = Flask(__name__)
visitors = Visitors()

@app.route('/')
def main_page():
    return visitors.on_main_show()


@app.route('/new_visitor', methods=['POST'])
def new_visitor():
    name = request.form.get('fname')
    surname = request.form.get('lname')
    return visitors.on_new_visitor(name, surname)


@app.route('/show_visitors')
def show_visitors():
    return visitors.on_visitors_show()


@app.route('/delete_visitors')
def delete_visitors():
    return visitors.on_delete_visitors()


if __name__ == "__main__":
    app.run()

