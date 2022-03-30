from abc import ABCMeta, abstractmethod


class ProductA(ABCMeta):
    @abstractmethod
    def do_stuff(cls):
        pass


class ProductB(ABCMeta):

    @abstractmethod
    def do_stuff(cls):
        pass


class AbstractFactory(ABCMeta):

    @abstractmethod
    def create_product_a(cls):
        pass

    @abstractmethod
    def create_product_b(cls):
        pass
