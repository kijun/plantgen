from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import random
grammar = CFG.fromstring(open("g3.txt").read())
print(grammar)
for sentence in generate(grammar, depth = 10):
    if random.random() < pow(0.5, 10):
        print(' '.join(sentence))

