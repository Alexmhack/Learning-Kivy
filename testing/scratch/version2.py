from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3
        self.add_widget(Label(text=""))
        self.add_widget(Label(text="Second col in the row"))
        self.add_widget(Label(text=""))


class VersionApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    VersionApp().run()
