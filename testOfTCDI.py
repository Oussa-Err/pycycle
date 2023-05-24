
from magazin import Magazin
from PRODUCT_TCDI import Product
from CLIENT_TCDI import Client

C = Client()

try:
    # p = Product(id=12, path=54, price=75)
    # print(p.getId())
    pClient = C(id=434, nom='oroborus', prenom='Erra', telephone='0621390221')
    result = pClient(id(int))
    print(result)

except Exception as ex:
    print(ex)


