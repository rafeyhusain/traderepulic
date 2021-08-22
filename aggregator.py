from datetime import datetime
from threading import Thread

from db import Db
from candlestick import CandleStick
from instrument_stream import InstrumentStream
from candlestick import CandleStick
from popular_instrument_list import PopularInstrumentList

class Aggregator():
	def __init__(self):
		self.db = Db()
		self.popular_list = PopularInstrumentList()
		self.__stop = False


	def start(self):
		thread = Thread(target = self.start_thread)
		thread.start()


	def start_thread(self):
		print("Starting Aggregator...")
		
		stream = InstrumentStream()
		for event in stream.read():
			if (self.__stop):
				break
			else:
				self.save_event(event)


	def stop(self):
		self.__stop


	def save_event(self, event):
		# TODO: Performance increase with cache
		candlestick = CandleStick(self.db.get(event["id"]))
		save = False

		if (candlestick.is_new):
			candlestick.id = event["id"]
			candlestick.openTimestamp = event["timestamp"]
			candlestick.openPrice = event["price"]
			save = True
		else:
			if(float(event["price"]) > candlestick.highPrice):
				candlestick.highPrice = event["price"]
				save = True

			if(float(event["price"]) < candlestick.lowPrice):
				candlestick.lowPrice = event["price"]
				save = True

			# If 30 minutes have passed, save close price and timestamp
			if(self.minutes(event["timestamp"], candlestick.openTimestamp) >= 30):
				candlestick.closePrice = event["price"]
				candlestick.closeTimestamp = event["timestamp"]
				save = True

		# TODO: Performance increase with batch update
		if (save):
			self.db.save(event["id"], candlestick.dict)
			self.popular_list.add(candlestick)


	def minutes(self, d1, d2):
		d1 = datetime.fromtimestamp(d1)
		d2 = datetime.fromtimestamp(d2)

		return (d1-d2).days * 24 * 60
