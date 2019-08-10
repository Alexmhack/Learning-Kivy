from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3
        self.add_widget(Label())
        self.add_widget(TextInput(text="Username", multiline=False))
        self.add_widget(Label())


class VersionApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    VersionApp().run()
