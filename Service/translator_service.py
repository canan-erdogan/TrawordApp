from translate import Translator


class TranslatorService:
    @staticmethod
    def translate(word):
        return Translator(from_lang="tr", to_lang="en").translate(word)