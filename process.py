import sys
import string

words = {}

for line in sys.stdin:
    tokens = line.split("\t")
    ngram, freq = tokens[0].lower(), int(tokens[2])
    if "_" in ngram:
        ngram = ngram[: ngram.index("_")]
    alpha = True
    for c in ngram:
        if c not in string.ascii_lowercase:
            alpha = False
            break
    if not alpha:
        continue
    if ngram in words.keys():
        words[ngram] += freq
    else:
        words[ngram] = freq

for ngram in words:
    print("%s,%d" % (ngram, words[ngram]))
