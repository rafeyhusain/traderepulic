from flask_restful import Resource
from db import Db
from candlestick import CandleStick

class Instruments(Resource):
	def get(self, id):
		db = Db()
		
		candlestick = CandleStick(db.get(id))

		# TODO: For performance use in-memory cachelike redis
		#  and bulk SQL update
		if (not candlestick.is_new):
			candlestick.views += 1

			db.save(id, candlestick.dict)

		return candlestick.dict
