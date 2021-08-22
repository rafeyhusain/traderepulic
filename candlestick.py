class CandleStick:
    def __init__(self):
        self.dict = self.default


    def __init__(self, in_dict):
        if (in_dict == None):
            in_dict = self.default

        self.dict = in_dict


    @property
    def default(self):
        return { 
			  "id": 0
			, "views": 0
			, "openTimestamp": 0
			, "openPrice": 0
			, "highPrice" : 0
			, "lowPrice": 0
			, "closePrice" : 0
			, "closeTimestamp" : 0
			}

    @property
    def id(self):
        return self.dict["id"]

    
    @id.setter
    def id(self, value):
        self.dict["id"] = int(value)


    @property
    def views(self):
        return self.dict["views"]

    
    @views.setter
    def views(self, value):
        self.dict["views"] = int(value)
        

    @property
    def openTimestamp(self):
        return self.dict["openTimestamp"]

    
    @openTimestamp.setter
    def openTimestamp(self, value):
        self.dict["openTimestamp"] = value
        
    
    @property
    def openPrice(self):
        return self.dict["openPrice"]

    
    @openPrice.setter
    def openPrice(self, value):
        self.dict["openPrice"] = float(value)
        
    
    @property
    def highPrice(self):
        return self.dict["highPrice"]

    
    @highPrice.setter
    def highPrice(self, value):
        self.dict["highPrice"] = float(value)
        
    
    @property
    def lowPrice(self):
        return self.dict["lowPrice"]

    
    @lowPrice.setter
    def lowPrice(self, value):
        self.dict["lowPrice"] = float(value)
        
    
    @property
    def closePrice(self):
        return self.dict["closePrice"]

    
    @closePrice.setter
    def closePrice(self, value):
        self.dict["closePrice"] = float(value)
        
    
    @property
    def closeTimestamp(self):
        return self.dict["closeTimestamp"]

    
    @closeTimestamp.setter
    def closeTimestamp(self, value):
        self.dict["closeTimestamp"] = value
        

    def get(self, id):
        candlestick = self.db.get_candlestick(id)

        return candlestick        

    
    @property
    def is_new(self):
        return self.dict == None or self.id == 0
		
	