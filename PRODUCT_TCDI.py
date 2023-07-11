class Product:
    def __init__(self, path, price):
        id = Product.auto
        id += 1
        self.setId(id)
        self.setPath(path)
        self.setPrice(price)

    auto = 0

    @staticmethod
    def setId(auto):
        auto += 1

    def setPath(self, path):
        if len(path) > 0:
            self.__path = path
        else:
            ex = Exception(self)
            raise ex

    def setPrice(self, price):
        if price > 0:
            self.__price = price
        else:
            ex = Exception(self)
            raise ex

    def getPath(self):
        return self.__path

    def getPrice(self):
        return self.__price

    def getId(self):
        return self.__id

    def __str__(self):
        return 'id: ' + str(self.__id) + '\t | price: ' + str(self.__price) + '\t | path: ' + self.__path

    def show(self):
        print(self)

