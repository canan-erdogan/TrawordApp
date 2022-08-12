import csv
import os.path


class WordService:
    def __init__(self, word, translated_word):
        self.word = word
        self.translated_word = translated_word
        if not os.path.exists("../Service/words.csv"):
            self.create_csv()
        self.append_word_to_csv()

    def create_csv(self):
        header = ["word", "translated_word"]
        self.write_to_csv(header)

    @staticmethod
    def write_to_csv(data):
        with open("../Service/words.csv", "a", encoding='UTF8', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(data)
        f.close()

    def append_word_to_csv(self):
        data = [self.word, self.translated_word]
        self.write_to_csv(data)


    @staticmethod
    def read_words_from_csv():
        if os.path.exists("../Service/words.csv"):
            reader = open("../Service/words.csv", "r", encoding='UTF8')
            return csv.DictReader(reader)
        return {}


