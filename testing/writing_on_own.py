import kivy
import requests
import json

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class DataInputPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.cols = 1


class TestApp(App):
	def build(self):
		return Label(text="Hey")


if __name__ == '__main__':
	TestApp().run()
