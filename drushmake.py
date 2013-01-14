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
PATCH = Keyword('patch').suppress()
URL = Keyword('url').suppress()
MD5 = Keyword('md5').suppress()
SUBDIR = Keyword('subdir').suppress()
OVERWRITE = Keyword('overwrite').suppress()
TRUTH = oneOf('TRUE FALSE')
DOWNLOAD = Keyword('download').suppress()
BRANCH = Keyword('branch').suppress()
TAG = Keyword('tag').suppress()
REVISION = Keyword('revision').suppress()
LIBRARIES = Keyword('libraries').suppress()
DESTINATION = Keyword('destination').suppress()

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

patch_name = Word(alphas, alphanums + '_-')('patch')
url = Word(printables)('url')
patch_url = (brackets(patch_name) + brackets(URL) | brackets(Optional(patch_name))) + EQUAL + url
patch_md5 = brackets(patch_name) + brackets(MD5) + EQUAL + Word(hexnums)('md5')
patch = brackets(PATCH) + (patch_url | patch_md5)

subdir = brackets(SUBDIR) + EQUAL + Word(printables)('subdir')

overwrite = brackets(OVERWRITE) + EQUAL + TRUTH('overwrite')

download_type = brackets(TYPE) + EQUAL + oneOf('git file svn bzr')('type')
download_url = brackets(URL) + EQUAL + url
download_hash = brackets(oneOf('md5 sha1 sha256 sha512')('algorithm')) + EQUAL + Word(hexnums)('hash')
download_branch = brackets(BRANCH) + EQUAL + Word(printables)('branch')
download_tag = brackets(TAG) + EQUAL + Word(printables)('tag')
download_revision = brackets(REVISION) + EQUAL + Word(hexnums)('revision')
download_option = download_type | download_url | download_hash | download_branch | download_tag | download_revision
download = (brackets(DOWNLOAD) + download_option)('download')

project_options = download | overwrite | patch | subdir | types | version
projects = (PROJECTS + brackets(name) + project_options)('projects')

libraries_destination = brackets(DESTINATION) + EQUAL + Word(printables)('destination')
libraries_download = (brackets(DOWNLOAD) + (download_type | download_url | download_hash))('download')
libraries_option = libraries_download | libraries_destination
libraries = (LIBRARIES + brackets(name) + libraries_option)('libraries')

makefile_grammar = (comment | ((api | core | projects | libraries) + Optional(comment))) + stringEnd

def parseline(line):
  def collapsespaces(chars):
    return ' '.join(chars.split())

  if line == '':
    return ()
  else:
    tokens = makefile_grammar.parseString(collapsespaces(line))
    return tokens
