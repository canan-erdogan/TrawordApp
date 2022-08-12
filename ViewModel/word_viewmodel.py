from Model.word import Word
from Service.word_service import WordService


class WordViewmodel:
    def __init__(self):
        self.words = []
        self.set_words_from_csv()

    def append_word_to_words(self, text, translated_text):
        word = Word(text, translated_text)
        self.words.append(word)
        WordService(word.word, word.translated_word)

    def set_words_from_csv(self):
        for row in WordService.read_words_from_csv():
            self.words.append(Word(row["word"], row["translated_word"]))
