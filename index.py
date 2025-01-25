from tokenizer import Tokenizer

with open("resources/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = Tokenizer.from_text(raw_text)
encoded = tokenizer.encode("you, -- and I.")

print(encoded)
print(tokenizer.decode(encoded))