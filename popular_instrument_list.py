from candlestick import CandleStick
from db import Db
import json 

class PopularInstrumentList:
    def __init__(self):
        self.db = Db()
        self.list = []


    def add(self, newItem):
        # save no more than 10 item
        if (len(self.list) < 10):
            self.list.append(newItem.dict)
            self.db.save("popular", self.list)
            return True

        # TODO: Search algorithm should be improved
        # replace existing popular item if new item has more views.
        # Also take care of sort listed of view count instead of replacement.
        for index, item in enumerate(self.list):
            candlestick = CandleStick(item)
            if (candlestick.views < newItem.views):
                self.list[index] = newItem
                self.db.save("popular", json.dumps(self.list))
                return True
  
        return False