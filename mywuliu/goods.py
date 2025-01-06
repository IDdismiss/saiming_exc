from flask import Blueprint, render_template

goods_bp = Blueprint("goods", __name__, template_folder="templates_goods")


@goods_bp.route("/add")
def add():
    return render_template("add.html")
