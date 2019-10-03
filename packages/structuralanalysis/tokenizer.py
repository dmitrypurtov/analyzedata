from yargy.tokenizer import MorphTokenizer

TOKINIZER = MorphTokenizer()
tokens = list(TOKINIZER("стали"))
print(tokens)
