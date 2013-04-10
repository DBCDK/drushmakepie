#from pyparsing import *
from tokens import *

def brackets(x):
  """ Helper function to enclose something in brackets. """
  return LBRCKT.leaveWhitespace() + x.leaveWhitespace() + RBRCKT.leaveWhitespace()

## Comment ##
optional_text = Combine(Optional(Word(printables + ' ')))
comment = HASH + optional_text('comment')

## Api ##
api_no = Word(nums)
api = API + EQUAL + api_no('api')

## Core ##
major_x = Combine(Word(nums) + Literal('.x'))
core = CORE + EQUAL + major_x('core')

## General definitions ##
# Name
name = Word(alphas, alphanums + '_')('name')

# Url
url = Word(printables)('url')

# Patch
patch_name = Word(alphas, alphanums + '_-')('patch')
patch_url = (brackets(patch_name) + brackets(URL) | brackets(Optional(patch_name))) + EQUAL + url
patch_md5 = brackets(patch_name) + brackets(MD5) + EQUAL + Word(hexnums)('md5')
patch = brackets(PATCH) + (patch_url | patch_md5)

# Subdir
subdir = brackets(SUBDIR) + EQUAL + Word(printables)('subdir')

# Overwrite
overwrite = brackets(OVERWRITE) + EQUAL + TRUTH('overwrite')

# Download
download_type = brackets(TYPE) + EQUAL + oneOf('git file svn bzr')('type')
download_url = brackets(URL) + EQUAL + url
download_hash = brackets(oneOf('md5 sha1 sha256 sha512')('algorithm')) + EQUAL + Word(hexnums)('hash')
download_branch = brackets(BRANCH) + EQUAL + Word(printables)('branch')
download_tag = brackets(TAG) + EQUAL + Word(printables)('tag')
download_revision = brackets(REVISION) + EQUAL + Word(hexnums)('revision')
download_option = download_type | download_url | download_hash | download_branch | download_tag | download_revision
download = (brackets(DOWNLOAD) + download_option)('download')

## Projects ##
# Version
short_version = EQUAL + Combine(Word(nums) + Literal('.') + Word(nums))('version')
long_version = brackets(VERSION) + short_version
version = short_version | long_version

# Type
types = brackets(TYPE) + EQUAL + oneOf('theme module core profile')('type')

# Project definition
project_options = download | overwrite | patch | subdir | types | version
projects = (PROJECTS + brackets(name) + project_options)('projects')

## Libraries ##
# destination
destination = brackets(DESTINATION) + EQUAL + Word(printables)('destination')

# Library definition
libraries_option = download | destination
libraries = (LIBRARIES + brackets(name) + libraries_option)('libraries')

## Grammar ##
statement = (comment | ((api | core | projects | libraries) + Optional(comment)))
grammar = ZeroOrMore((statement)) + stringEnd
