from flask import Blueprint, render_template, request, flash, redirect

import db

goods_bp = Blueprint("goods", __name__, template_folder="templates_goods")


# 商品列表
@goods_bp.route("/list")
def list():
    # 获取所有商品的信息
    sql = """
        select * from goods where is_actived = 1;
    """
    goods = db.query_data(sql)
    return render_template("list.html", goods=goods)


@goods_bp.route("/search", methods=["POST"])
def search():
    name = request.form.get("name")

    sql = f"""
        select * from goods 
        where name like "%{name}%" and is_actived=1;
    """
    goods = db.query_data(sql)
    print(goods)
    return render_template("list.html", goods=goods)


# 新增商品
@goods_bp.route("/add")
def add():
    return render_template("add.html")


@goods_bp.route("/doadd", methods=["POST"])
def doadd():
    name = request.form.get("name")
    price = request.form.get("price")
    unit = request.form.get("unit")

    if name and price and unit:
        sql = f"""
            insert into goods
            values(null, "{name}", {price}, "{unit}", CURRENT_TIME, CURRENT_TIME, 1)
        """
        db.insert_or_update_data(sql)
        return redirect("/goods/list")
    else:
        flash("请完整填写内容！")
        return redirect("/goods/add")


@goods_bp.route("/view")
def view():
    id = request.args.get("id")

    sql = f"""
        select * from goods
        where id = {id};
    """
    good = db.query_data(sql)
    good = good[0]
    return render_template("view_good.html", good=good)


@goods_bp.route("/edit")
def edit():
    id = request.args.get("id")
    sql = f"""
        select * from goods
        where id = {id}
     """

    good = db.query_data(sql)
    good = good[0]
    return render_template("edit_good.html", good=good)


@goods_bp.route("/doedit", methods=["POST"])
def doedit():
    id = request.args.get("id")
    price = request.form.get("price")
    unit = request.form.get("unit")
    print(id, price, unit)

    sql = f"""
        update goods set price={price}, unit="{unit}", update_time=CURRENT_TIME WHERE ID = {id};
    """
    db.insert_or_update_data(sql)
    flash("修改成功")
    return redirect("/goods/list")


@goods_bp.route("/del")
def delbyid():
    id = request.args.get("id")
    sql = f"""
        update goods set is_actived=2 where id = {id}
    """

    db.insert_or_update_data(sql)
    flash("用户已删除！")
    return redirect("/goods/list")
