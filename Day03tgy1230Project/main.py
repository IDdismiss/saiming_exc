import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <h1>hello 张子佳</h1>
    <img src = "http://bd.xitong18.com/style/images/bd_logo1.png" />
    <img src = "https://bip3.seentao.com/iuap-uuas-tenant/ucf-wh/account/images/BIPlogo.png" />
    
    """


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/goods")
def goods():
    title = "商品信息"
    # 字典类型
    dict = {
        "title": "红心火龙果....",
        "price": 99,
        "src": "https://img20.360buyimg.com/jdcms/s240x240_jfs/t1/220392/7/20954/204562/646b8e57Fc117ab6a/39b80c447188f804.jpg.avif"
    }
    # 列表类型
    list=[
        {
            "id": "001",
            "title": "春节购物卡",
            "price": 199,
            "src": "https://img11.360buyimg.com/jdcms/s240x240_jfs/t1/267240/25/638/388818/67650cdaF4376a4f3/966cbc3696d76df5.jpg.avif"
        },
        {
            "id": "002",
            "title": "凤凰牌自行车",
            "price": "299",
            "src": "https://img11.360buyimg.com/jdcms/s240x240_jfs/t1/268169/38/3103/108230/676be8b1F3ebb84ac/ddeecae65c410a96.jpg.avif"
        },
        {
            "id": "003",
            "title": "猫粮",
            "price": 399,
            "src": "https://img13.360buyimg.com/jdcms/s240x240_jfs/t1/185049/13/49651/98247/670cba2fFba82f64e/d27d12c6e95d0e4e.jpg.avif"
        }
    ]
    return render_template("goods.html", dict=dict, title=title, list=list)


@app.route("/users/<userid>")
def users(userid):
    # 和数据库交互， 根据用户id获取用户的相关信息
    print(userid)
    return f"""
        <h1>userid: {userid}</h1>
    """


@app.route("/getdatas")
def getdatas():
    data = [
            {
                "id": "001",
                "title": "新年好....."
            },
            {
                "id": "002",
                "title": "你也新年好....."
            }
        ]
    return json.dumps({
        "msg": "success",
        "data": data
    })


@app.route("/login", methods=["POST"])
def login():
    # 获取用户名 密码
    # 和数据库交互
    flag = True
    if flag:
        return json.dumps({
            "msg": "success"
        })
    else:
        return json.dumps({
            "msg": "error"
        })


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
