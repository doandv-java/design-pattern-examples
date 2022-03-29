from abc import ABC, abstractmethod

from creational.factory_method.exercise.button.button import Button


class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        ok_button = self.create_button()
        ok_button.onclick()
        ok_button.render()
