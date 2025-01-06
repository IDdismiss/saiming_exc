from flask import Blueprint, render_template, request, redirect, flash, json, session
import db

users_bp = Blueprint("users", __name__, template_folder="templates_users")


# 用户登录
@users_bp.route("/login")
def login():
    return render_template("login.html")


@users_bp.route("/dologin", methods=["POST"])
def dologin():
    # 获取表单数据，输入的用户名 密码
    username = request.form.get("username")
    password = request.form.get("password")

    # 和数据库交互
    sql = f"""
        select * from users
        where username="{username}" and password="{password}"
    """

    data = db.query_data(sql)
    if data:
        print("登录成功")
        user = data[0]
        # 把字典转换为json
        user = json.dumps(user)
        # 存一个用户登录成功的标识
        session["user"] = user

        return ""

    else:
        flash("用户名或密码错误")
        return redirect("/login")


# 用户注册
@users_bp.route("/register")
def register():
    return render_template("register.html")


@users_bp.route("/doregister", methods=["POST"])
def doregister():
    # 获取表单数据
    username = request.form.get("username")
    password = request.form.get("password")
    tel = request.form.get("tel")
    gender = request.form.get("gender")
    city = request.form.get("city")
    # 和数据库交互
    #
    if username and password:
        sql = f"""
            insert into users
            values(null, "{username}", "{password}", "{tel}", "{gender}", "{city}", 2, "", CURRENT_TIME, CURRENT_TIME, 1)
        """
        db.insert_or_update_data(sql)
        return "注册成功"
    else:
        flash("用户或密码不能为空")
        return redirect("/register")


# 退出登录

@users_bp.route("/logout")
def logout():
    return render_template("logout.html")


# 用户列表
@users_bp.route("/userlist")
def userlist():
    # 获取所有用户的信息

    # 返回一个页面并传值
    return render_template("userslists.html")
