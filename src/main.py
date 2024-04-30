from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Label
        self.add_widget(Label(text='Enter your name:'))

        # Text Input
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        # Button
        self.button = Button(text='Submit')
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

        # Result Label
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def on_button_press(self, instance):
        name = self.name_input.text
        self.result_label.text = f'Hello, {name}!'

class MyApp(App):
    def build(self):
        return MyForm()

if __name__ == '__main__':
    MyApp().run()
