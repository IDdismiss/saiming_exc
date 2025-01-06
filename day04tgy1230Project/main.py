from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return """
    <h1>hello world</h1>
    <h1>hello python</h1>
    <h1>hello flask</h1>    
    """


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("news")
def news():
    return render_template("news.html")


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run()

