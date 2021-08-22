import threading

from storage_api import StorageAPI

class Db():
	def __init__(self, start = 0):
		self.sql_db = StorageAPI()
		self.lock = threading.Lock()


	def reset(self):
		self.sql_db.store = {}

		self.sql_db.save("items", {})
		self.sql_db.save("popular", {})


	def get(self, key):
		self.lock.acquire()
		try:
			dict = self.sql_db.get(str(key))
			
			return dict
		finally:
			self.lock.release()


	def save(self, key, payload):
		self.lock.acquire()
		try:
			self.sql_db.save(key, payload)
		finally:
			self.lock.release()
