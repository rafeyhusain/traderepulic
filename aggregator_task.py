from flask_restful import Resource
from aggregator import Aggregator

class AggregatorTask(Resource):
	def get(self):
		# TODO: For maintainability scheduled or background tasks
		# should be handled in one unified way
		aggregator = Aggregator()
		aggregator.start()

		return "Aggregator thread is started..."
