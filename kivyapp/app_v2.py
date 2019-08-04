import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ConnectPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		# dividing the window in two cols
		self.cols = 2

		# widget defined first stacks in the first col
		self.add_widget(Label(text="IP:"))
		self.ip = TextInput(multiline=False)
		# this widget goes into second col
		self.add_widget(self.ip)

		# third widget takes up a seperate row and so on
		self.add_widget(Label(text="Port:"))
		self.port = TextInput(multiline=False)
		self.add_widget(self.port)

		self.add_widget(Label(text="Username:"))
		self.username = TextInput(multiline=False)
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


class EpicApp(App):
	def build(self):
		return ConnectPage()


if __name__ == '__main__':
	EpicApp().run()
