from webapp import webapp
from flask import jsonify
from flask import request
from flask import render_template
from flask import abort
import pymongo


@webapp.route('/')
@webapp.route('/index')
def index():
    return render_template("index.html", title="Главная страница")


@webapp.route("/api/")
@webapp.route("/api/orders")
# @webapp.route("/api/<method>", methods=["GET"])
def orders(method=None):
    return f"Method {method} API not ready"


@webapp.route("/api/add_order/", methods=["GET"])
def add_order():
    request_data = request.form
    return request_data


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

