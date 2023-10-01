class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item,'price': price,'quantity': quantity}
        self.cart.append(product)
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price']*item['quantity']
        print('total price:',total)
        if amount<total:
            print (f'plz provide {total-amount} more')
        else:
            extra = amount-total
            print(f'here is your extra money:',extra)

dora = Shopping('Dora')
dora.add_to_cart('potato',50,6)
dora.add_to_cart('egg',12,24)
dora.add_to_cart('rice',50,5)
print(dora.cart)

# dora.checkout(600)
dora.checkout(1600)