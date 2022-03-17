from flask import Flask
from flask_restx import Api,Namespace,Resource

app = Flask(__name__)
api = Api(app)
name_ns = Namespace('parse demo', description='By myself')


class ParseDemo(Resource):
    get_parser = api.parser()
    get_parser.add_parser()

    @name_ns.expect(get_parser)
    def get(self):
        return {"code": 0, "msg": "success"}


if __name__ == '__main__':
    app.run(debug=True)
