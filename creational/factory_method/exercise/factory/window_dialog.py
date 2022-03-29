from creational.factory_method.exercise.button.button import Button
from creational.factory_method.exercise.button.window_button import WindowButton
from creational.factory_method.exercise.factory.dialog import Dialog


class WindowDialog(Dialog):
    def create_button(self) -> Button:
        return WindowButton()

    def render(self):
        print("WinDialog")
        super().render()
