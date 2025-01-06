from flask import Flask, render_template
from users import users_bp
from goods import goods_bp

app = Flask(__name__)
app.secret_key = 'SkMax'

# 注册蓝图对象
app.register_blueprint(users_bp)
app.register_blueprint(goods_bp, url_prefix="/goods")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
