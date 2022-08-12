from kivy.lang import Builder
from kivy.uix.textinput import TextInput

from Service.translator_service import TranslatorService
from ViewModel.word_viewmodel import WordViewmodel

Builder.load_file("kv/traword_box_content_textinput.kv")


class TrawordBoxContentTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_text_validate= self.on_enter)
        self.word_viewmodel = WordViewmodel()

    def on_enter(self, value):
        translated_text = TranslatorService().translate(self.text)
        self.parent.children[0].children[1].text = self.text
        self.parent.children[0].children[0].text = translated_text
        self.word_viewmodel.append_word_to_words(self.text, translated_text)
        self.text = ""



