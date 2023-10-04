class Product:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock

class Shop:
    def __init__(self) -> None:
        self.products=[]

    def add_product(self,name,price,stock):
        new_product=Product(name,price,stock)
        self.products.append(new_product)

    def buy_product(self,product_name):
        for product in self.products:
            if product.name==product_name:
                if product.stock>0 :
                    product.stock-=1
                    return f'Congratulations'
                else :
                    return f'{product_name} is not available in stock'
        return f'{product_name} is not in shop'
    
dalia = Shop()
dalia.add_product('lip balm',250,5)
dalia.add_product('Nail polish',150,10)
print(dalia.buy_product('lip balm'))
print(dalia.buy_product('Nail polish'))
