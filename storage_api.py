import json

class StorageAPI():
	store = {}

	def save(self, key, payload):
		self.store[key] = payload
		with open('keystore.json', 'w') as f:
			json.dump(self.store, f)

	def get(self, key):
		with open('keystore.json', 'r') as f:
			self.store = json.load(f)
		return self.store.get(key,None)

	def load(self):
		with open('keystore.json', 'r') as f:
			self.store = json.load(f)
		return self.store


if __name__ == '__main__':
	storage = StorageAPI()
	storage.save('a', 1)
	print(storage.get('b'))
	print(storage.get('a'))