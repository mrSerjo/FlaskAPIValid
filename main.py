from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class InnModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inn_num = db.Column(db.String, nullable=False)

    def __repr__(self):
        return {'Номер ИНН': f"{self.inn_num}"}

# При первом запуске скрипта снять коммент для создания базы данных
# db.create_all() # После создания базы данных можно удалить или закомментировать


class Check_inn(Resource):

    def get(self, inn_num):
        this_num = InnModel.query.filter_by(inn_num=inn_num).first()
        if not this_num is None:
            return {"data": inn_num, "status": "already in database"}
        if inn_num.isdigit() and (len(inn_num) == 10 or len(inn_num) == 12):
            return {"data": inn_num, 'status': 'is_valid'}
        else:
            return {"data": inn_num, 'status': 'is_not_valid'}


    def put(self, inn_num):
        new_inn = InnModel(inn_num=inn_num)
        db.session.add(new_inn)
        db.session.commit()
        return {"data": inn_num, "status": "now in database"}

api.add_resource(Check_inn, "/check_inn/<string:inn_num>")


if __name__ == "__main__":
    app.run(debug=True)

