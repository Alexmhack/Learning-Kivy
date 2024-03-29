import os
import requests

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


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
        self.add_widget(self.fetch)

    def fetch_button(self, instance):
        city = self.city.text
        country = self.country.text

        test_app.display_weather_page.fetch_weather(city, country)
        test_app.screen_manager.current = "DisplayWeather"


class DisplayWeatherPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_key = os.getenv('API_KEY')
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={},{}"

        self.send_url = "&appid=" + self.api_key

        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_message_width)
        self.add_widget(self.message)

        self.back = Button(text="Go Back")
        self.back.bind(on_press=self.back_button)
        self.add_widget(self.back)

    def back_button(self, instance):
        test_app.screen_manager.current = "DataInput"

    def update_message_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

    def fetch_weather(self, city, country):
        response = requests.get(self.url.format(city, country) + self.send_url)
        response_json = response.json()
        try:
            temp = int((response_json['main']['temp'] - 273.15))
            condition = response_json['weather'][0]['main']
            message = "Weather Report for {0} is {1} with {2} degree celcius\
            ".format(city, condition, temp)
        except Exception as e:
            print(e)
            message = "Error getting weather details, try again later."

        self.message.text = message


class TestApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.data_input_page = DataInputPage()
        screen = Screen(name="DataInput")
        screen.add_widget(self.data_input_page)
        self.screen_manager.add_widget(screen)

        self.display_weather_page = DisplayWeatherPage()
        screen = Screen(name="DisplayWeather")
        screen.add_widget(self.display_weather_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    test_app = TestApp()
    test_app.run()
