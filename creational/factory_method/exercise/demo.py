from creational.factory_method.exercise.factory.dialog import Dialog
from creational.factory_method.exercise.factory.web_dialog import WebDialog
from creational.factory_method.exercise.factory.window_dialog import WindowDialog


class Application:
    dialog: Dialog

    def initialize(self, os_name: str):
        if os_name == 'Windows':
            self.dialog = WindowDialog()
        elif os_name == 'web':
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system")

    def main(self, os_name: str):
        self.initialize(os_name)
        self.dialog.render()


if __name__ == '__main__':
    os_name = 'web'
    application = Application()
    application.main(os_name)
