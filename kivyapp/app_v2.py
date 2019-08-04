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
		self.add_widget(Label(text="Username:"))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="Port:"))
		self.port = TextInput(multiline=False)
		self.add_widget(self.port)

		self.join = Button(text="Join")
		self.add_widget(Label())
		self.add_widget(self.join)


class EpicApp(App):
	def build(self):
		return ConnectPage()


if __name__ == '__main__':
	EpicApp().run()
