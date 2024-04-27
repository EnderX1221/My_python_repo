from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='This is a Label'))
        self.add_widget(Button(text='This is a Button'))

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
from kivy.uix.button import Button

# Creating a button with custom styling
button = Button(
    text='Click Me',
    size_hint=(None, None),
    size=(200, 50),
    color=(1, 1, 1, 1),
    font_size='20sp',
    background_color=(0, 0, 1, 1)  # RGBA
)
class MyButtonApp(App):
    def build(self):
        button = Button(text='Press Me')
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        instance.text = 'You Pressed Me!'
        print('Button pressed!')

if __name__ == '__main__':
    MyButtonApp().run()
# main.py
from kivy.app import App
from kivy.lang import Builder

Builder.load_file('my.kv')

class MyApp(App):
    def build(self):
        return Builder.load_file('my.kv')

if __name__ == '__main__':
    MyApp().run()
