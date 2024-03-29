import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


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

        self.cols = 2

        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label())
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(self.join)

    def join_button(self, instance):
        ip = self.ip.text
        port = self.port.text
        username = self.username.text

        with open("prev_details.txt", "w") as file:
            file.write(f"{ip},{port},{username}")

        # add text to message using method
        info = f"Attempting to join {ip}:{port} as {username}"
        chat_app.info_page.update_info(info)

        # change the current screen to Info
        chat_app.screen_manager.current = "Info"


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)

        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

        self.back = Button(text="Go Back")
        self.back.bind(on_press=self.back_button)
        self.add_widget(self.back)

    def back_button(self, instance):
        chat_app.screen_manager.current = "Connect"

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    chat_app = EpicApp()
    chat_app.run()
