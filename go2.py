from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import random
grammar = CFG.fromstring(open("g3.txt").read())
print(grammar)
for depth in range(0, 30):
    print(depth)
    with open("filteredlines%02d.txt" % (depth), "w") as f:
        last = ""
        cnt = 0
        for sentence in generate(grammar, depth=depth):
            if random.random() < pow(0.7, depth):
                cnt += 1
                last = ' '.join(sentence) + "\n"
                if cnt > 50:
                    break
                f.write(last)
                f.flush()
        f.write(last)


