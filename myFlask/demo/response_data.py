"""处理响应信息"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/text")
def get_text():
    return "文本信息"


@app.route("/tuple")
def get_tuple():
    return "元组信息", 201


@app.route("/json")
def get_json():
    return jsonify(status=0, message="success !")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
