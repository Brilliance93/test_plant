from flask import Flask, request
from flask_restx import Api, Namespace, Resource, fields
from werkzeug.datastructures import FileStorage

from demo.log_util import logger

app = Flask(__name__)
api = Api(app)
name_ns = Namespace('parse demo', description='By myself')


@name_ns.route('')
class ParseDemo(Resource):
    get_parser = api.parser()
    get_parser.add_argument('param', type=str, location='args')
    get_parser.add_argument('age', type=int, location='args')
    get_parser.add_argument('choice', choices=('girls', 'boys'), location='args')
    get_parser.add_argument('file', type=FileStorage, location='files')
    get_parser.add_argument('password', type=str, help='this is password', location='form', required=True)
    # json 不可以和其他类型一起出现
    # get_parser.add_argument('username', type=str, help='this is username', location='json', required=True)

    @name_ns.expect(get_parser)
    def get(self):
        logger.info(f"request.args=====>{request.args}")
        return {"code": 0, "msg": "success"}

    post_parser = api.parser()
    post_parser.add_argument('username', type=str, help='this is username', location='json', required=True)
    post_parser.add_argument('password', type=int, help='this is password', location='json', required=True)

    @name_ns.expect(post_parser)
    def post(self):
        logger.info(f"request.json===>{request.json}")
        return {"code": 0, "msg": "success"}


api.add_namespace(name_ns, '/login')


if __name__ == '__main__':
    app.run(debug=True)
