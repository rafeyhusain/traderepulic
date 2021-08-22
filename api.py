from flask import Flask
from flask_restful import Api

from instruments import Instruments
from popular_instruments import PopularInstruments
from aggregator_task import AggregatorTask

app = Flask(__name__)

api = Api(app)

api.add_resource(AggregatorTask, '/')
api.add_resource(Instruments, '/instruments/<int:id>')
api.add_resource(PopularInstruments, '/instruments/popular')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
