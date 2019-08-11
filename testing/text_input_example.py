import kivy

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

kivy.require('1.11.1')


class TextInputExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username"))
        self.add_widget(TextInput(multiline=False))


class SampleApp(App):
    def build(self):
        return TextInputExample()


if __name__ == '__main__':
    SampleApp().run()
