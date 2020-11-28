from webapp import webapp
from webapp.forms import AddOrderForm
from flask import jsonify
from flask import request
from flask import flash
from flask import render_template
from flask import redirect
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


@webapp.route("/add-order", methods=["GET", "POST"])
def add_order():
    form = AddOrderForm()
    if form.validate_on_submit():
        flash('Order name {0} type is {1}'.format(form.order_name.data, form.order_type.data))
        return redirect("/index")
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

