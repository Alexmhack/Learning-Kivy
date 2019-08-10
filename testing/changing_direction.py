import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen  # , FadeTransition

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
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.FadeTransition
# screen_manager = ScreenManager(transition=FadeTransition())
screen_manager.add_widget(MenuScreen(name='menu'))
screen_manager.add_widget(SettingsScreen(name='settings'))


class TestApp(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    TestApp().run()
