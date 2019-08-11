# Learning-Kivy
Learning to develop cross platform applications using the python Kivy library.

## Installation
Follow the instructions on the kivy official [website](https://kivy.org/#download) for your
operating system and install the latest version of kivy.

Optionally you can install the kivy examples which are by the way very useful for learning
the code base of other kivy applications, install the examples using,

```
python -m pip install kivy_examples==1.11.1
```

**1.11.1** is the latest version of kivy as of today, yours might be different or same, anyway
install it, if you get any errors google it and there are is a huge community of kivy developers
who have answered many questions related to many problems.

Hopefully you have installed all of this inside a virtualenv as in the instructions given
during installation, so now inside you virtualenv start by writing your first kivy app.

## First App
Code is [here](https://github.com/Alexmhack/Learning-Kivy/blob/master/kivyapp/app_v0.py)

Create a new python file naming it whatever you want and inside it write your basic kivy *App*

```
import kivy

from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1') # replace with your current kivy version !
```

We will be subclassing the kivy **App** and implementing its **build()** method to return
a widget instance.

```
...
class TestApp(App):
    def build(self):
        return Label(text="Hey there")


if __name__ == '__main__':
    TestApp().run()
```

Here we create a object of our *App* class and call its *run* method, you can also do the same
using,

```
if __name__ == '__main__':
    test_app = TestApp()
    test_app.run()
```

Now run `python your-file-name.py` and if your kivy installation is fine then a window will
appear with the *Label* `Hey there` in the center of the window.

## Grid Layout
Code can be in **testing/grid_layout_example.py**\
So just like we align rows and columns in HTML and CSS, kivy is somewhat similar but with
little less customizable. You can use the `kivy.uix.gridlayout` to divide the layout into
columns and place widgets in the layouts or create layouts inside a layout itself.

Using grid layout is very simple, you can just import it and divide the layout first by,

```
from kivy.uix.gridlayout import GridLayout

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 # diving the layout into two cols
```

Now we need to add widgets into our columns, the order of adding widgets will be the same
order in which the widgets are displayed in the layout.

For example, we add widgets into the layout using,

```
class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 # diving the layout into two cols

        self.add_widget(Label(text="First column in the layout."))
        self.add_widget(Label(text="Second column."))
```

Now that we have divided the layout into two columns, adding two widgets like we did above will
place the labels side by side on the same screen.

## Text Input
code piece is in **testing/text_input_example.py**
For taking input from the users kivy has input fields like the `TextInput`, we can place this
field in one of the column and a label in the second column for e.g.

```
from kivy.uix.textinput import TextInput
...

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 # diving the layout into two cols

        self.add_widget(Label(text="First column in the layout."))
        self.add_widget(TextInput(multiline=False))
...
```

Import `TextInput` from `kivy.uix.textinput` and use it simple by creating a instance of it
like the code piece above, `multiline=False` will make sure that the input from the user does
not go in the second line (multiline).

Run the file just like you would run any python program and you will find the text input in
the second column of the layout in which you can enter your input.

Now try adding more *Label* and *TextInput* in the same way and you will find that the labels
and inputs will be placed in their respective columns and row.

## Button & Events
code is in **testing/button_event_eg.py**

Lets move on and build a chat application using kivy and python sockets. (I have followed the
tutorial from [sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfwnDTZWw8H3hN_VRQfq8rF))

So to know when user wants to connect to the chat socket we need to provide the user a button
and catch the event from the button to finally connect.

Kivy has *Button* for this,

```
from kivy.uix.button import Button

# moving on with out connect page
class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 # diving the layout into two cols

        # add or change this if you haven't
        self.add_widget(Label(text="IP Address:"))
        self.add_widget(TextInput(multiline=False))

        self.add_widget(Label(text="Port:"))
        self.add_widget(TextInput(multiline=False))

        self.add_widget(Label(text="Username:"))
        self.add_widget(TextInput(multiline=False))

        self.join = Button(text="Join")
        self.add_widget(self.join)
```

The button will be placed in the first column leaving the second column empty, so we can
add a empty *Label* in the second column making it look a little good.

```
        ...
        self.join = Button(text="Join")
        self.add_widget(Label())
        self.add_widget(self.join)
```

Now what is left is making the button work or binding an method to the button click / press
event. We will be doing this by using the `.bind` method of `Button` instance.

```
        ...
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text
        print(f"Attempting to join {ip}:{port} as {username}")
```

**Note:** Following the tutorial, I have also implemeted the initial filling of input fields
by writing them to a file first and then reading from the file on next run of App.

You can find this implementation in the same file.
