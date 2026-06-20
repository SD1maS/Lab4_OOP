import re

class Letter:
    def __init__(self, char: str):
        self.char = char

    def __str__(self):
        return self.char

class Punctuation:
    def __init__(self, char: str):
        self.char = char

    def __str__(self):
        return self.char

class Word:
    def __init__(self, string_word: str):
        self.letters = [Letter(char) for char in string_word]

    def length(self) -> int:
        return len(self.letters)

    def __str__(self):
        return "".join(str(l) for l in self.letters)

class Sentence:
    def __init__(self, raw_text: str):
        cleaned_text = re.sub(r'[ \t]+', ' ', raw_text.strip())
        self.raw = cleaned_text
        self.elements = []
        
        tokens = re.findall(r'\w+|[^\w\s]', self.raw)
        for token in tokens:
            if re.match(r'\w+', token):
                self.elements.append(Word(token))
            else:
                self.elements.append(Punctuation(token))
                
        words_only = [el for el in self.elements if isinstance(el, Word)]
        self.word_count = len(words_only)
        self.letter_count = sum(w.length() for w in words_only)

    def __eq__(self, other):
        if not isinstance(other, Sentence):
            return False
        return self.raw.lower() == other.raw.lower()

    def __str__(self):
        return f"Речення: '{self.raw}' | Слів: {self.word_count}, Літер: {self.letter_count}"

class SentenceManager:
    @staticmethod
    def sort_sentences(sentences: list[Sentence]) -> list[Sentence]:
        return sorted(sentences, key=lambda s: (s.word_count, -s.letter_count))

    @staticmethod
    def find_same(sentences: list[Sentence], target: Sentence) -> int:
        for i, item in enumerate(sentences):
            if item == target:
                return i
        return -1


def main():
    sentences_array = [
        Sentence("Код працює добре!"),
        Sentence("Тут є\t\tбагато різних слів."),
        Sentence("Це тестове речення."),
        Sentence("Це дуже коротке."),
        Sentence("Код працює   добре!")
    ]

    target_sentence = Sentence("це ТеСтОвЕ речення.")

    print("\033[1mПочатковий масив:\033[0m")
    for s in sentences_array:
        print(s)

    sorted_sentences = SentenceManager.sort_sentences(sentences_array)

    print("\n\033[1mВідсортований масив (Слова ↑, Літери ↓):\033[0m")
    for s in sorted_sentences:
        print(s)

    print("\n\033[1mПошук заданого об'єкта:\033[0m")
    print(f"Шукаємо: '{target_sentence.raw}'")

    index = SentenceManager.find_same(sorted_sentences, target_sentence)

    if index != -1:
        print(f"Об'єкт знайдено. Індекс у відсортованому масиві: {index}")
    else:
        print("Об'єкт не знайдено.")

if __name__ == "__main__":
    main()