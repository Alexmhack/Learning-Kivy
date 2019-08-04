import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
	BoxLayout:
		Button:
			text: 'Goto settings'
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.current = 'settings'
		Button:
			text: 'Quit'

<SettingsScreen>:
	BoxLayout:
		Button:
			text: 'My settings button'
		Button:
			text: 'Back to menu'
			on_press:
				root.manager.transition.direction = 'right'
				root.manager.current = 'menu'
""")


# declare both screens
class MenuScreen(Screen):
	pass


class SettingsScreen(Screen):
	pass


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name='Menu'))
screen_manager.add_widget(SettingsScreen(name='Settings'))


class TestApp(App):
	def build(self):
		return screen_manager


if __name__ == '__main__':
	TestApp().run()
