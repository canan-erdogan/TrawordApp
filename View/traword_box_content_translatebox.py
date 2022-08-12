from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_file("kv/traword_box_content_translatebox.kv")

class TrawordBoxContentTranslatebox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        word = Label(font_size=30)

        translated_word = Label(font_size=30)

        self.add_widget(word)
        self.add_widget(translated_word)