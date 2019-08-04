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
