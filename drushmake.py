from pyparsing import *


LBRCKT = Literal('[').suppress()
RBRCKT = Literal(']').suppress()
EQUAL = Literal('=').suppress()
HASH = oneOf('# ;').suppress()
API = Keyword('api').suppress()
CORE = Keyword('core').suppress()
PROJECTS = Keyword('projects').suppress()
optional_text = Combine(Optional(Word(printables + ' ')))
comment = HASH + optional_text('comment')
api_no = Word(nums) | Word(nums)
api = API + EQUAL + api_no('api')
major_x = Combine(Word(nums) + Literal('.x'))
core = CORE + EQUAL + major_x('core')
name = Word(alphas, alphanums + '_')('name')
version = Combine(Word(nums) + Literal('.') + Word(nums))('version')
projects = (PROJECTS + LBRCKT + name + RBRCKT + EQUAL + version)('projects')


makefile_grammar = comment | ((api | core | projects) + Optional(comment))

def parseline(line):
  def collapsespaces(chars):
    return ' '.join(chars.split())

  if line == '':
    return ()
  else:
    tokens = makefile_grammar.parseString(collapsespaces(line))
    return tokens
