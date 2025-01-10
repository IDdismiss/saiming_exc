from datetime import datetime

from flask import Blueprint, render_template, request, redirect
import db

# 定义蓝图对象
customers_bp = Blueprint("customers", __name__)


# 列表
@customers_bp.route("/list")
def list():
    sql = f"""
            select * from customers where is_actived = 1;
        """
    customers = db.query_data(sql)
    return render_template("customers/list.html", customers=customers)


@customers_bp.route("/add")
def add():
    return render_template("customers/add.html")


@customers_bp.route("/add_cus", methods=["post"])
def add_cus():
    cname = request.form.get("cname")
    tel = request.form.get("tel")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")
    address = request.form.get("address")

    sql = f"""
        insert into customers
        values(null,"{cname}",{tel},"{birthday}","{gender}","{address}",CURRENT_TIME,CURRENT_TIME,1);
    """

    db.insert_or_update_data(sql)

    return redirect("/customers/list")


@customers_bp.route("/search", methods=["post"])
def search():
    cname = request.form.get("cname")
    tel = request.form.get("tel")

    sql1 = f"""
        select * from customers where cname like "%{cname}%" and is_actived = 1;
    """
    sql2 = f"""
            select * from customers where tel = "{tel}" and is_actived = 1;
        """
    sql3 = f"""
                select * from customers where cname like "%{cname}%" and tel = "{tel}" and is_actived = 1;
            """
    if cname and tel:
        customers = db.query_data(sql3)
    elif tel:
        customers = db.query_data(sql2)
    elif cname:
        customers = db.query_data(sql1)
    else:
         redirect("/customers/list")
    return render_template("customers/list.html", customers=customers)


@customers_bp.route("/chakan1")
def chakan():
    id = request.args.get("id")

    sql = f"""
        select * from customers where id = {id};
    """
    customer = db.query_data(sql)
    # print(data)
    customer = customer[0]
    print(customer)
    return render_template("customers/chakan1.html", customer=customer)


@customers_bp.route("/bianji1")
def bianji():
    id = request.args.get("id")
    sql = f"""
        select * from customers where id = {id};
    """
    customer = db.query_data(sql)
    customer = customer[0]
    print(customer)
    return render_template("customers/bianji1.html", customer=customer)


@customers_bp.route("/do_bianji1", methods=["post"])
def do_bianji():
    id = request.args.get("id")
    cname = request.form.get("cname")
    tel = request.form.get("tel")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")
    address = request.form.get("address")
    current_time = datetime.now()

    sql = f"""
        update customers set cname="{cname}",tel="{tel}",birthday="{birthday}",gender="{gender}",address="{address}",update_time="{current_time}" where id = {id};
    """

    db.insert_or_update_data(sql)
    return redirect("/customers/list")


@customers_bp.route("/shanchu1")
def shanchu():
    id = request.args.get("id")
    update_time = datetime.now()

    sql=f"""
        update customers set is_actived = 2, update_time = "{update_time}" where id = {id}
    """

    db.insert_or_update_data(sql)
    return redirect("/customers/list")