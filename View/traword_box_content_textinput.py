from kivy.lang import Builder
from kivy.uix.textinput import TextInput

from Service.translator_service import TranslatorService

Builder.load_file("kv/traword_box_content_textinput.kv")


class TrawordBoxContentTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_text_validate= self.on_enter)

    def on_enter(self, value):
        self.parent.children[0].children[1].text = self.text
        self.parent.children[0].children[0].text = TranslatorService().translate(self.text)
        self.text = ""


