import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require('1.11.1')


class GridPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="First Column"))
        self.add_widget(Label(text="Second Column"))


class SampleApp(App):
    def build(self):
        return GridPage()


if __name__ == '__main__':
    sample_app = SampleApp()
    sample_app.run()
