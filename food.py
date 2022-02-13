class Food(object):
    def __init__(self, name:str, URL:str , image_URL:str):
        self.name = name
        self.URL = URL
        self.image_URL = image_URL


    def __key(self):
        return (self.name, self.URL, self.image_URL)

    
    def __hash__(self):
        return hash(self.__key())

    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Food):
            return self.__key() == other.__key()
        return NotImplemented