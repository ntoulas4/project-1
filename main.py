from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     btn = Button(text="click me", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.5})
    #     self.label = Label(text="Nothng", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.6})
    #     self.textInput = TextInput(size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.7}, multiline=False)
    #     self.textInput.bind(on_text_validate=self.display)
    #     btn.bind(on_press=self.display)
    #     self.add_widget(self.textInput)
    #     self.add_widget(self.label)
    #     self.add_widget(btn)
    def display(self):
        data = self.ids.textInput.text
        self.ids.label.text = data

class ProjectApp(App):
    pass
    # def build(self):
    #     return Interface()


ProjectApp().run()
