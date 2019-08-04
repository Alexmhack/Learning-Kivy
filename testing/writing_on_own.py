import kivy
import requests

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class DataInputPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.cols = 1


class DisplayWeatherPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.api_key = 'eb1ed9135fc15fd78e986d8824d4fd69'
		self.url = "http://api.openweathermap.org/data/2.5/weather?q={},India"

		self.send_url = "&appid=" + self.api_key


class TestApp(App):
	def build(self):
		return Label(text="Hey")


if __name__ == '__main__':
	TestApp().run()
