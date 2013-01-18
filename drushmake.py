from makegrammar import *


def parseline(line):
  def collapsespaces(chars):
    return ' '.join(chars.split())

  if line == '':
    return ()
  else:
    tokens = grammar.parseString(collapsespaces(line))
    return tokens
