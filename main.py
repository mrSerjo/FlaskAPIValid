from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


inns = {}


class Check_inn(Resource):
    def get(self, inn_num):
        if inn_num.isdigit() and (len(inn_num) == 10 or len(inn_num) == 12):
            return {"data": inn_num, 'status': 'is_valid'}
        else:
            return {"data": inn_num, 'status': 'is_not_valid'}


api.add_resource(Check_inn, "/check_inn/<string:inn_num>")


if __name__ == "__main__":
    app.run(debug=True)

