#!/usr/local/bin/python3
# JSON is hard, lets use shell.
# grep quote quotaculous.json | sed 's/^.*:"\(.*\)",$/\1/' | grep -v 'var quotes' > quotaculous.txt
#
# https://quotaculous.appspot.com/a/quotaculous.json


import sys
import json
import random

END = 0

def NormalizeWord(word):
  word = word.lower()
  word = word.replace('.', '')
  return word


def main(argv):
  # chain = {
  #  'word': ['trailing word', 'another', END]  # no deduping
  # }

  chain = {}
  quotes = open('quotaculous.txt').readlines()
  starting_words = []
  for quote in quotes:
    quote = quote.strip()
    quote = quote.split()
    for i, word in enumerate(quote):
      word = NormalizeWord(word)

      if i == 0:
        starting_words.append(word)

      if i == len(quote) - 1:
        trailing_word = END
      else:
        trailing_word = NormalizeWord(quote[i+1])
      chain[word] = chain.setdefault(word, []) + [trailing_word]

  for x in xrange(20):
    # walk the chain.
    quote = []
    word = random.choice(starting_words)
    while word != END:
      quote.append(word)
      word = random.choice(chain[word])
    quote = ' '.join(quote)
    quote += '.'
    quote = quote.capitalize()
    print quote


if __name__ == '__main__':
  main(sys.argv)
