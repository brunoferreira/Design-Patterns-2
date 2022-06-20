class PizzaComponent:

    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Dough(PizzaComponent):
    cost = 0.5


class Decorator(PizzaComponent):
    
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Cheese(Decorator):

    cost = 1.5
    
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Tomato(Decorator):

    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Onion(Decorator):

    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class TomatoSauce(Decorator):

    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Pepperoni(Decorator):

    cost = 7.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Ham(Decorator):

    cost = 6.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


if __name__ == "__main__":
    hamPizza = Ham(Cheese(TomatoSauce(Dough())))
    print(hamPizza.getDescription()+ ": $" + str(hamPizza.getTotalCost()))
    pepperoniPizza = Pepperoni(Onion(Cheese(TomatoSauce(Dough()))))
    print(pepperoniPizza.getDescription()+ ": $" + str(pepperoniPizza.getTotalCost()))