from flask import Flask
from log_util import logger
from markupsafe import escape

app = Flask(__name__)

@app.route('/demo/<string:username>')
def hello_falsk(username):
 logger.info(f"this name is:{username}")
 return f"this name is:{username}"

@app.route("/testcase",methods=["get"])
def get_case():
 return {"code":0,"msg":"Get Success"}

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
 app.run(debug=True)