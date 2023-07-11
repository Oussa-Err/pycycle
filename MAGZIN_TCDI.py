from PRODUCT_TCDI import Product
import pickle

class Magazin:
    def __init__(self):
        self.prod = []

    def getProd(self):
        return self.__prod

    def setProd(self, prod):
        self.__prod = prod

    def append(self):
        self.__prod.append(Product)

    def __del__(self):
        print('Product deleted')

    def show(self):
        for prod in self.__prod:
            prod.show()

    def exist(self, id):
        match = False
        for product in self.__product:
            if product == id:
                match = product
                break
            return match

    def find(self, id):
        match = None
        for product in self.prod:
            if product.getId() == id:
                match = True
                break
            return match

    def save(self):
        file = open('product.bin', 'w')
        pickle.dump(self.__prod, file)

    def load(self):
        file = open('product.bin', 'rb')
        self.__prod = pickle.load(file)
        file.close()

# if __name__=='__main__':
