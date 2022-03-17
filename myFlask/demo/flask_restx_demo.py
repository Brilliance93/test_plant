from flask import Flask
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
api = Api(app, version='2.0', description='描述信息')
user_ns = Namespace("demo", description="demo学习")


# 方法一：1、@api.route() 通过该方式定义路由，可要可不要。后续可以通过add_resource方式增加
# 将路径定义在类上
# 方法二：使用命名空间
@user_ns.route("")
class User(Resource):
    @user_ns.doc(params={'ID': "An ID"})
    def get(self):
        return {"code": 0, "message": "get success"}

    post_model = api.model('PostModel', {
        'name': fields.String(required=True, description='This is name'),
        'sex': fields.String(required=True, description='sex choice', enum=['boy', 'girl']),
        'age': fields.Integer(description='how old are you?', min=0),
    })

    @user_ns.doc(body=post_model)
    def post(self):
        return {"code": 0, "message": "post success"}

    def put(self):
        return {"code": 0, "message": "put success"}

    def delete(self):
        return {"code": 0, "message": "delete success"}


# 方法一：2、通过add_resource(类名，路径)将url路径指定到对应资源上
# api.add_resource(User, '/case')

api.add_namespace(user_ns, "/case")


if __name__ == '__main__':
    app.run(debug=True)
