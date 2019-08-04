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

		self.city = TextInput(text="Enter your city")
		self.add_widget(self.city)

		self.country = TextInput(text="Enter your country")
		self.add_widget(self.country)

		self.fetch = Button(text="Show Weather")
		self.fetch.bind(on_press=self.fetch_button)


class DisplayWeatherPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.api_key = 'eb1ed9135fc15fd78e986d8824d4fd69'
		self.url = "http://api.openweathermap.org/data/2.5/weather?q={},India"

		self.send_url = "&appid=" + self.api_key

	def fetch_weather(self, city):
		response = requests.get(self.urlurl.format(city) + self.send_url)
		response_json = response.json()
		try:
			temp = int((response_json['main']['temp'] - 273.15))
			condition = response_json['weather'][0]['main']
			message = "Weather Report for {0} is {1} with {2}degree celcius".format(
				city, condition, temp)
		except Exception as e:
			print(e)
			message = "Error getting weather details, try again later."

		self.message.text = message


class TestApp(App):
	def build(self):
		return Label(text="Hey")


if __name__ == '__main__':
	test_app = TestApp()
	test_app.run()
