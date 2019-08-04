import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class ConnectPage(GridLayout):
    pass


class EpicApp(App):
    def build(self):
        return ConnectPage()


if __name__ == '__main__':
    EpicApp().run()
