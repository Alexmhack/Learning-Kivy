from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="IP Address:"))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Userame:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class VersionApp(App):
    def build(self):
        return ConnectPage()


if __name__ == '__main__':
    VersionApp().run()
