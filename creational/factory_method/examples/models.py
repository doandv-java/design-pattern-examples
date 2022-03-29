from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def do_stuff(self):
        pass


class ProductA(IProduct):

    def do_stuff(self):
        pass


class ProductB(IProduct):
    def do_stuff(self):
        pass


class BaseFactory(ABC):
    @abstractmethod
    def create_product(self) -> IProduct:
        pass


class ProductAFactory(BaseFactory):

    def create_product(self) -> IProduct:
        return ProductA()


class ProductBFactory(BaseFactory):

    def create_product(self) -> IProduct:
        return ProductB()
