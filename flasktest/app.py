from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify

app = Flask(__name__)

#jsonify支持中文
app.config['JSON_AS_ASCII'] = False

users = [
    {
        "username": "123",
        "password": "123"
    }
]

# @app.route('/')
# def index():
#      return render_template("index.html")

#
# @app.route('/send_message', methods=['GET','POST'])
# def send_message():
#
#     global message_get
#     message_get = ""
#
#     message_get = request.args['message']
#     print("收到前端发过来的信息：%s" % message_get)
#     print("收到数据的类型为：" + str(type(message_get)))
#     return "后台收到消息"
#
#
# @app.route('/change_to_json', methods=['GET'])
# def change_to_json():
#
#     global message_get
#     message_json = {
#         "message": message_get
#     }
#     return jsonify(message_json)
#     #return  make_response(jsonify(message_json), 200)

@app.route('/')
def index():
      return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
# 创建登陆页面路由, 数据传输方法为GET/POST
def login():
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        for user in users:
            if user['username'] == username and user['password'] == password:
                #  将用户登录的信息存储到session中
                #session['user'] = username
                resu = {
                    "code":200,
                    "message":'登录成功'
                }
                #data_json = json.dumps(resu,ensure_ascii=False)
                #return resu
                #redirect 重定向
                #return redirect(url_for('index'))
                return jsonify(resu)
            else:
                # 出现一个闪现信息
                #flash("用户%s密码错误， 请重新登录....." % (username))
                #return redirect(url_for('login'))
                resu = {
                    "code":200,
                    "message":'登录失败'
                }
                return jsonify(resu)


if __name__ == '__main__':
    app.run()

