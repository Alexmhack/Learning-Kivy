import kivy
import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ConnectPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		if os.path.isfile("prev_details.txt"):
			with open("prev_details.txt", "r") as f:
				file = f.read().split(",")

			prev_ip = file[0]
			prev_port = file[1]
			prev_username = file[2]
		else:
			prev_ip = ""
			prev_port = ""
			prev_username = ""

		# dividing the window in two cols
		self.cols = 2

		# widget defined first stacks in the first col
		self.add_widget(Label(text="IP:"))
		self.ip = TextInput(text=prev_ip, multiline=False)
		# this widget goes into second col
		self.add_widget(self.ip)

		# third widget takes up a seperate row and so on
		self.add_widget(Label(text="Port:"))
		self.port = TextInput(text=prev_port, multiline=False)
		self.add_widget(self.port)

		self.add_widget(Label(text="Username:"))
		self.username = TextInput(text=prev_username, multiline=False)
		self.add_widget(self.username)

		self.join = Button(text="Join")
		# bind this button for an event to a method
		self.join.bind(on_press=self.join_button)
		self.add_widget(Label())
		self.add_widget(self.join)

	def join_button(self, instance):
		port = self.port.text
		ip = self.ip.text
		username = self.username.text

		print(f"Attempting to join {ip}:{port} as {username}")

		with open('prev_details.txt', 'w') as file:
			file.write(f"{ip},{port},{username}")


class EpicApp(App):
	def build(self):
		return ConnectPage()


if __name__ == '__main__':
	EpicApp().run()
