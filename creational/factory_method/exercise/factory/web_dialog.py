from creational.factory_method.exercise.button.button import Button
from creational.factory_method.exercise.button.html_button import HTMLButton
from creational.factory_method.exercise.factory.dialog import Dialog


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()

    def render(self):
        print("WebDialog")
        super().render()
