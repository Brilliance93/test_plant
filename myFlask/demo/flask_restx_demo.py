from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app)

user_ns = Namespace("demo", description="demo学习")


# @api.route() 通过该方式定义路由，可要可不要。后续可以通过add_resource方式增加
# 将路径定义在类上
@user_ns.route()
class User(Resource):
    def get(self):
        return {"code": 0, "message": "get success"}

    def post(self):
        return {"code": 0, "message": "post success"}

    def put(self):
        return {"code": 0, "message": "put success"}

    def delete(self):
        return {"code": 0, "message": "delete success"}


# 通过add_resource(类名，路径)增加路由
# api.add_resource(User, '/case')

api.add_namespace(user_ns, "/case")


if __name__ == '__main__':
    app.run(debug=True)
