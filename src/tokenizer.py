import re

UNKNOWN = "<|unknown|>"
END_OF_TEXT = "<|endoftext|>"

class Tokenizer:
    def __init__(self, vocab: dict[str, int]):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text: str) -> list[int]:
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int else UNKNOWN for item in preprocessed
        ]
        ids = [self.str_to_int[item] for item in preprocessed]
        return ids

    def decode(self, ids: list[int]) -> str:
        text = " ".join([self.int_to_str[item] for item in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r"\1", text)
        return text

    @staticmethod
    def from_text(text: str):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        all_words = sorted(set(preprocessed))

        all_words.extend([END_OF_TEXT, UNKNOWN])

        vocab = {token: integer for integer, token in enumerate(all_words)}

        return Tokenizer(vocab)
