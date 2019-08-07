import kivy
from kivy.app import App
from kivy.uix.label import Label

# run only in this version of kivy
kivy.require('1.11.1')


# App requries only build
class EpicApp(App):
    def build(self):
        return Label(text='Hey there')


if __name__ == '__main__':
    EpicApp().run()
