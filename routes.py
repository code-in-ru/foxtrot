from webapp import webapp
from webapp.forms import AddOrderForm
from flask import jsonify
from flask import request
from flask import flash
from flask import render_template
from flask import redirect
from flask import abort
import pymongo
import sqlite3


@webapp.route('/')
@webapp.route('/index')
def index():
    return render_template("index.html", title="Главная страница")


@webapp.route("/api", methods=["GET"])
@webapp.route("/api/orders", methods=["GET"])
# @webapp.route("/api/<method>", methods=["GET"])
def orders(method=None):
    return {"name": ["apples, oranges"]}\


@webapp.route("/addorder", methods=["GET", "POST"])
def add_order():
    form = AddOrderForm()
    if form.validate_on_submit():
        with sqlite3.connect("data/rosatom.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO tasks (author, title, type, description)
            VALUES (?, ?, ?, ?);""", (form.author.data, form.title.data, form.task_type.data, form.description.data))
            task_id = cursor.lastrowid
            conn.commit()
            flash("Task have id={0}".format(task_id))
        return redirect("/")
    return render_template("add_order.html", title="Добавление ордера", form=form)


@webapp.route("/todo", methods=["GET"])
def todo():
    return f"Method todo API not ready"


@webapp.route("/master", methods=["GET", "POST"])
def master():
    if request.method == "POST":
        request_data = request.form
    else:
        request_data = None
    return render_template("master.html", request_data=request_data)

