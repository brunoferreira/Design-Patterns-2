from abc import abstractmethod

class Creator():
    """
    - Design Pattern Factory -
    Classe abstrata para instanciadores de veículos.
    """

    @abstractmethod
    def createVehicle(self):
        pass


class TruckCreator(Creator):
    """
    - Design Pattern Factory -
    Classe deriavada de Creator para instanciador de caminhões.
    """

    def createVehicle(self):
        return Truck()


class CarCreator(Creator):
    """
    - Design Pattern Factory -
    Classe deriavada de Creator para instanciador de carros.
    """

    def createVehicle(self):
        return Car()


class MotorcycleCreator(Creator):
    """
    - Design Pattern Factory -
    Classe deriavada de Creator para instanciador de motocicletas.
    """

    def createVehicle(self):
        return Motorcycle()


class Vehicle():
    """
    - Design Pattern Bridge -
    Classe de veículos.
    """

    def __init__(self):
        self.motor = None

    def set_motor(self, motor):
        """
        - Design Pattern Bridge -
        Define o tipo de motor do veículo.

        Parameters
        ----------
        motor : Motor
            Motor a ser definido.

        Examples
        --------
        >>> my_electric_motor = ElectricMotor()
        >>> Vehicle.set_motor(my_electric_motor)
        """
        self.motor = motor


class Truck(Vehicle):
    """
    - Design Pattern Bridge -
    Classe de caminhões. Herda classe de veículos.
    """

    def __init__(self):
        super().__init__()


class Car(Vehicle):
    """
    - Design Pattern Bridge -
    Classe de carros. Herda classe de veículos.
    """

    def __init__(self):
        super().__init__()


class Motorcycle(Vehicle):
    """
    - Design Pattern Bridge -
    Classe de motocicletas. Herda classe de veículos.
    """

    def __init__(self):
        super().__init__()


class Motor():
    """
    - Design Pattern Bridge -
    Classe de motores.
    """

    def __init__(self):
        pass


class ElectricMotor(Motor):
    """
    - Design Pattern Bridge -
    Classe de motores elétricos. Herda classe de motores.
    """

    def __init__(self):
        super().__init__()


class HybridMotor(Motor):
    """
    - Design Pattern Bridge -
    Classe de motores híbridos. Herda classe de motores.
    """

    def __init__(self):
        super().__init__()


class CombustionMotor(Motor):
    """
    - Design Pattern Bridge -
    Classe de motores a combustão. Herda classe de motores.
    """

    def __init__(self):
        super().__init__()