from flask import Flask,render_template
import json
from flask import request
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#bootstrap = Bootstrap(app)



# 使用当前的模板测试，就是将当前的html静态页面放在当前的templates
# @app.route('/login/')
# @app.route('/login/<name>')
# def login():
#     # assert name is not None 断言的简单使用
#     return render_template('login.html'),200

@app.route('/')
def to_login_page():
    return render_template("login.html")

@app.route("/json",methods=['GET', 'POST'])
def json_result():
    return {"username": "张三", "age": 18, "pwd": "123456"}  # 如果返回的数据为字典类型的数据默认会转换为json数据返回




@app.route("/login", methods=["POST"])
def login():
    loginName = request.form["loginName"]
    loginPwd = request.form["loginPwd"]
    if loginName == "admin" and loginPwd == "admin":
        print("login success")
        return render_template("index.html", loginName=loginName)
    else:
        return render_template("login.html", msg="用户名或密码错误！")


@app.route("/addUser", methods=["GET", "POST"])
def get_form_params():
    # 使用三元表达式写入请求的方式
    method_way = "POST" if request.method == "POST" else "GET"
    username = None
    # 通过当前的request.form[] 方式获取的是post请求传递的参数，不能用于get请求获取参数，如果参数不存在的话就会报错
    if "username" in request.form:  # 用于处理post请求的数据，一般用于处理表单提交的数据
        username = request.form["username"]
    elif "username" in request.args:  # 一般用于当前的get请求传递的参数或者数据
        username = request.args["username"]
    return "当前使用的请求方式为：{0}，传递的参数为：{1}".format(method_way, username)





@app.route('/user/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def user():
    if request.method == 'GET':

        return 'get'
    elif request.method == 'POST':

        return 'post'
    elif request.method == 'DELETE':

        return 'delete'
    elif request.method == 'PATCH':

        return 'update'
    elif request.method == 'PUT':

        return 'put'

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True,port=1000, host='127.0.0.1')#debug=true进入调试状态
