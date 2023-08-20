class Basket:
    def __init__(self, model_name, basket_type, components):
        self.model_name = model_name
        self.components = components
        self.basket_type = basket_type
    def print_basket_info(self):
        components_joined = (',').join(self.components)
        print(f'This is a "{self.model_name}" model, which is an {} basket composed of the following: {components_joined}.')

class EquityBasket(Basket):
    def __init__(self, model_name, components):
        super().__init__(model_name=model_name, basket_type="equity", components=components)
    def print_considerations(self):
        print("Consider whether to invest in single stocks, futures or options.")

class CommodityBasket(Basket):
    def __init__(self, model_name, components):
        super().__init__(model_name=model_name, basket_type="commodity", components=components)
    def print_considerations(self):
        print("Consider whether to invest in futures or options.")