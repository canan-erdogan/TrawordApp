from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.traword_box_content_textinput import TrawordBoxContentTextInput
from View.traword_box_content_translatebox import TrawordBoxContentTranslatebox

Builder.load_file("kv/traword_box_content.kv")


class TrawordBoxContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TrawordBoxContentTextInput())
        self.add_widget(TrawordBoxContentTranslatebox())