class PizzaComponent:
    """
    - Design Pattern Decorator -
    Classe interface componente pizza.
    """

    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Dough(PizzaComponent):
    """
    - Design Pattern Decorator -
    Classe componente concreto massa de pizza.
    """
    
    cost = 0.5


class Decorator(PizzaComponent):
    """
    - Design Pattern Decorator -
    Classe decorador base.
    """
    
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Cheese(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto queijo.
    """
    
    cost = 1.5
    
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Tomato(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto tomate.
    """
    
    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Onion(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto cebola.
    """
    
    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class TomatoSauce(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto molho de tomate.
    """
    
    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Pepperoni(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto peperoni.
    """
    
    cost = 7.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Ham(Decorator):
    """
    - Design Pattern Decorator -
    Classe decorador concreto presunto.
    """
    
    cost = 6.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


if __name__ == "__main__":
    hamPizza = Ham(Cheese(TomatoSauce(Dough())))
    print(hamPizza.getDescription()+ ": $" + str(hamPizza.getTotalCost()))
    pepperoniPizza = Pepperoni(Onion(Cheese(TomatoSauce(Dough()))))
    print(pepperoniPizza.getDescription()+ ": $" + str(pepperoniPizza.getTotalCost()))
