import logging

from flask import Flask, escape, request
from log_util import logger

app = Flask(__name__)


# 定义动态路由
@app.route('/demo/<string:username>')
def hello_flask(username):
    logger.info(f"this name is:{username}")
    return f"this name is:{username}"


# 定义接口请求方式为get
@app.route("/testcase", methods=["get"])
def get_case():
    return {"code": 0, "msg": "Get Success"}


# 定义路由传参
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"  # escape 解析路径上的特殊符号


# 定义接口请求方式为post
@app.route("/login", methods=["post"])
def login_post():
    logger.info(request.json)
    return {"code": 0, "msg": "Post Success"}


# 定义接口请求方式为put，使用args传参
@app.route("/register", methods=["put"])
def request_put():
    username = request.args.get('name')
    print(username)
    # return {"code": 0, "msg": "put success"}
    return username


# 定义接口请求方式为put，处理前端发来的form数据
@app.route("/put", methods=["put"])
def put_method():
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    logger.info(request.form)
    return {"code": 0, "message": " put success", "name": name, "password": pwd}


# 处理前端上传的文件，并将文件保存到本地
@app.route("/file", methods=["post"])
def upload_file():
    file = request.files.get("file")
    logger.info(file)
    filename = file.filename
    logger.info(f"文件名为{filename}")
    file.save("./logo.png")
    return {"code": 0, "message": " upload file success"}


if __name__ == '__main__':
    app.run(debug=True)