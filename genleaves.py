from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import random
import os
rule_name = "rule1"
grammar = CFG.fromstring(open("rules/leaves/"+rule_name+".txt").read())
print(grammar)
dir_name = "generated/leaves/" + rule_name
if not (os.path.exists(dir_name)):
    os.mkdir(dir_name)
for depth in range(0, 30):
    print(depth)
    with open(dir_name + "/%02d.txt" % (depth), "w") as f:
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


