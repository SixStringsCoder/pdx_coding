import re

def display(storage: dict, qty=10) -> None:

    for key, count in sorted(storage.items(), key=lambda t: t[1], reverse=True)[:qty]:
        print(key, count)


def get_data(path: str) -> str:
    with open(path, 'r') as file:
        text = file.read()  # .read is a method on a file object that returns the file as a single string
        return text


def cleaner(multi_lined_text: str) -> str:

    de_punctify = re.sub(r'[.,]', '', multi_lined_text)
    lowercase_it = de_punctify.lower()

    return lowercase_it


def quantify_words(path: str) -> None:
    text = get_data(path)

    cleaned = cleaner(text).split()

    storage = dict()

    for words in cleaned:
        try:
            storage[words] += 1
        except KeyError:
            storage[words] = 1

    display(storage, qty=6)


path = '/Users/mbp/Git/PythonFullStack/1_Python/3_Applied_Python/labs/ari/books/jack_and_jill.txt'

quantify_words(path)