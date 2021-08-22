from flask_restful import Resource
from db import Db

class PopularInstruments(Resource):
    def get(self):
        db = Db()

        return db.get("popular")
