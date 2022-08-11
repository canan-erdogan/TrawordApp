from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


from kivy.uix.label import Label

Builder.load_file("kv/traword_box_title.kv")

class TrawordBoxTitle(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text= "Traword App", font_size= 45))

