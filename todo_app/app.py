import os
from flask import Flask, redirect, request, render_template
from todo_app.data.trello_items import get_items, add_item, move_item_to_done
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items = items)

@app.route('/add-todo', methods=["post"])
def add_todo():
    title = request.form.get('title')
    add_item(title)
    return redirect('/')

@app.route('/complete-item/<todo_id>', methods=["post"])
def complete_item(todo_id):
    move_item_to_done(todo_id)
    return redirect('/')