from __future__ import print_function
#from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import random
import os
import itertools
import sys
from nltk.grammar import Nonterminal

def generate(grammar, start=None, depth=None, n=None):
    """
    Generates an iterator of all sentences from a CFG.

    :param grammar: The Grammar used to generate sentences.
    :param start: The Nonterminal from which to start generate sentences.
    :param depth: The maximal depth of the generated tree.
    :param n: The maximum number of sentences to return.
    :return: An iterator of lists of terminal tokens.
    """
    if not start:
        start = grammar.start()
    if depth is None:
        depth = sys.maxsize

    iter = _generate_all(grammar, [start], depth)

    if n:
        iter = itertools.islice(iter, n)

    return iter


def _generate_all(grammar, items, depth):
    if items:
        try:
            for frag1 in _generate_one(grammar, items[0], depth):
                for frag2 in _generate_all(grammar, items[1:], depth):
                    yield frag1 + frag2
        except RuntimeError as _error:
            if _error.message == "maximum recursion depth exceeded":
                # Helpful error message while still showing the recursion stack.
                raise RuntimeError(
                    "The grammar has rule(s) that yield infinite recursion!!"
                )
            else:
                raise
    else:
        yield []


def _generate_one(grammar, item, depth):
    if depth > 0:
        if isinstance(item, Nonterminal):
            for prod in grammar.productions(lhs=item):
                returned = False
                prev_frag = None
                for frag in _generate_all(grammar, prod.rhs(), depth - 1):
                    prev_frag = frag
                    if random.random() < 0.5:
                        returned = True
                        yield frag
                        if random.random() < 0.1:
                            break
                if not returned:
                    yield prev_frag or []
        else:
            yield [item]

rule_name = "rule2"
grammar = CFG.fromstring(open("rules/leaves/"+rule_name+".txt").read())
print(grammar)
dir_name = "generated/leaves/" + rule_name
if not (os.path.exists(dir_name)):
    os.mkdir(dir_name)
with open(dir_name + "/gen.txt", "w") as f:
    for depth in range(0, 30):
        print(depth)
        last = ""
        cnt = 0
        for sentence in generate(grammar, depth=depth):
            cnt += 1
            last = ' '.join(sentence) + "\n"
            if cnt > 50:
                break
            f.write(last)
            f.flush()
        f.write(last)

