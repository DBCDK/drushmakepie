from pyparsing import *

# Symbols and basic tokens
LBRCKT = Literal('[').suppress()
RBRCKT = Literal(']').suppress()
EQUAL = Literal('=').suppress()
HASH = oneOf('# ;').suppress()
API = Keyword('api').suppress()
CORE = Keyword('core').suppress()
PROJECTS = Keyword('projects').suppress()
VERSION = Keyword('version').suppress()
TYPE = Keyword('type').suppress()

# Helper functions
def brackets(x):
  return LBRCKT + x + RBRCKT

# Comment
optional_text = Combine(Optional(Word(printables + ' ')))
comment = HASH + optional_text('comment')

# Api
api_no = Word(nums) | Word(nums)
api = API + EQUAL + api_no('api')

# Core
major_x = Combine(Word(nums) + Literal('.x'))
core = CORE + EQUAL + major_x('core')

# Projects
name = Word(alphas, alphanums + '_')('name')

short_version = EQUAL + Combine(Word(nums) + Literal('.') + Word(nums))('version')
long_version = brackets(VERSION) + short_version
version = short_version | long_version

types = brackets(TYPE) + EQUAL + oneOf('theme module core profile')('type')

projects = (PROJECTS + brackets(name) + (types | version))('projects')


makefile_grammar = comment | ((api | core | projects) + Optional(comment))

def parseline(line):
  def collapsespaces(chars):
    return ' '.join(chars.split())

  if line == '':
    return ()
  else:
    tokens = makefile_grammar.parseString(collapsespaces(line))
    return tokens
