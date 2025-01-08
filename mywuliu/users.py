import os.path
import random

from flask import Blueprint, render_template, request, redirect, flash, json, session
import db
import hashlib

users_bp = Blueprint("users", __name__, template_folder="templates_users")

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(["png", "jpg", "JPG", "PNG", "jpeg", "JPEG"])


# 封装一个方法，判断文件格式是否符合条件
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 用户登录
@users_bp.route("/login")
def login():
    return render_template("login.html")


@users_bp.route("/dologin", methods=["POST"])
def dologin():
    # 获取表单数据，输入的用户名 密码
    username = request.form.get("username")
    password = request.form.get("password")

    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    new_password = md5.hexdigest()

    # 和数据库交互
    sql = f"""
        select * from users
        where username="{username}" and password="{new_password}"
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
    # 获取上传文件
    file = request.files["file"]

    if not (file and allowed_file(file.filename)):
        flash("图片格式不正确！,请上传png，jpg， jpeg格式图片")
        return redirect("/register")

    # 获取项目的基础路径
    basepath = os.path.dirname(__file__)
    # 利用随机数生成一个数字
    randomid = round(random.uniform(1000, 2000))
    randomid = str(randomid)
    md5 = hashlib.md5()
    md5.update(randomid.encode("utf-8"))
    randomid = md5.hexdigest()

    filename = file.filename  # 获取上传文件名
    index = filename.index(".")  # 获取.的索引位置
    filename = randomid + filename[index:]

    # 上传
    upload_path = os.path.join(basepath, f'static/upload/{filename}')
    file.save(upload_path)

    # 保存到数据库的路径
    path = f"/static/upload/{filename}"

    # 和数据库交互
    if username and password:

        # 对密码进行MD5加密
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        new_password = md5.hexdigest()

        sql = f"""
            insert into users
            values(null, "{username}", "{new_password}", "{tel}", "{gender}", "{city}",
             2, "{path}", CURRENT_TIME, CURRENT_TIME, 1)
        """
        db.insert_or_update_data(sql)
        return "注册成功"
    else:
        flash("用户或密码不能为空")
        return redirect("/register")


# 用户列表
@users_bp.route("/userslist")
def userslist():
    # 获取所有用户的信息
    sql = """
        select * from users where is_actived=1;
    """
    users = db.query_data(sql)
    # pprint(users)
    # 返回一个页面并传值
    return render_template("userslist.html", users=users)


# 用户列表查询
@users_bp.route("/search", methods=["POST"])
def search():
    # 获取要查询的用户名
    username = request.form.get("username")
    # 查询语句
    sql = f"""
        select * from users 
        where username like "%{username}%" and is_actived=1;
    """
    users = db.query_data(sql)
    return render_template("userslist.html", users=users)


# 用户信息查看
@users_bp.route("/view")
def view():
    # 获取id
    id = request.args.get("id")
    # 和数据库交互，获取对应id的所有信息
    sql = f"""
        select * from users
        where id = {id};
    """
    user = db.query_data(sql)
    # user = user[0]
    # 返回页面，并传输数据
    return render_template("view.html", user=user)


# 编辑用户信息
@users_bp.route("/edit")
def edit():
    # 获取id
    id = request.args.get("id")
    # 和数据库交互，获取对应id的所有信息
    sql = f"""
        select * from users
        where id = {id};
    """
    user = db.query_data(sql)
    user = user[0]
    return render_template("edit.html", user=user)


@users_bp.route("/doedit", methods=["POST"])
def doedit():
    id = request.args.get("id")
    username = request.form.get("username")
    gender = request.form.get("gender")
    tel = request.form.get("tel")

    sql = f"""
        update users set username="{username}", gender="{gender}",
        tel="{tel}", update_time=CURRENT_TIME
        where id = {id};
    """
    db.insert_or_update_data(sql)
    return "修改成功"


# 删除用户
@users_bp.route("/del")
def delbyid():
    id = request.args.get("id")

    sql = f"""
        update users set is_actived = 2
        where id = {id} ;
    """
    db.insert_or_update_data(sql)
    flash("用户已删除")
    return redirect("/userslist")


# 退出登录
@users_bp.route("/logout")
def logout():
    return render_template("logout.html")
