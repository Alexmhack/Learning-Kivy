import kivy

from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class EpicApp(App):
    def build(self):
        return Label(text="Hey There")


if __name__ == '__main__':
    EpicApp().run()
