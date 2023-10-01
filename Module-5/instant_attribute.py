class Shop:
    shopping_mall = 'jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] #instant attribute

    def add_to_cart(self,item):
        self.cart.append(item)

dalia = Shop('Da lia')
dalia.add_to_cart('shoes')
dalia.add_to_cart('phone')
print(dalia.cart)

arkan = Shop('Arkar')
arkan.add_to_cart('cap')
arkan.add_to_cart('watch')
print(arkan.cart)