from pyparsing import *
from tokens import *

def brackets(x):
    """ Helper function to enclose something in brackets. """
    return (LBRCKT + x + RBRCKT).leaveWhitespace()

def optionallyQuoted(non_quoted):
    """ Helper function to enclose words without qoutes in optional """
    """ single or double quotes. """
    single_quoted = QuotedString("'", '\\')
    double_quoted = QuotedString('"', '\\')

    quoted = single_quoted | double_quoted
    quoted.setParseAction(lambda tokens: non_quoted.parseString(tokens[0]))
    return quoted | non_quoted

## Comment ##
optional_text = Combine(Optional(Word(printables + ' ')))
comment = HASH + optional_text('comment')

## Api ##
api_no = optionallyQuoted(Word(nums))
api = API + EQUAL + api_no('api')

## Core ##
major_x = optionallyQuoted(Combine(Word(nums) + Literal('.x')))
core = CORE + EQUAL + major_x('core')

## General definitions ##
# Name
name = optionallyQuoted(Word(alphas, alphanums + '_'))('name')

# Url
percent_encoded_chars = '(%[0-9a-fA-F]{2})'
url_chars = '[' + alphanums + ";/?:@=&$\-_.+!*'()," + ']' # escaped dash with \
url = optionallyQuoted(Regex('(' + url_chars + '|' + percent_encoded_chars + ')+'))('url')

# Patch
patch_name = Word(alphas, alphanums + '_-')('patch')
patch_url = (brackets(patch_name) + brackets(URL) | brackets(Optional(patch_name))) + EQUAL + url
patch_md5 = brackets(patch_name) + brackets(MD5) + EQUAL + optionallyQuoted(Word(hexnums))('md5')
patch = brackets(PATCH) + (patch_url | patch_md5)

# Subdir
subdir = brackets(SUBDIR) + EQUAL + optionallyQuoted(Word(printables))('subdir')

# Overwrite
overwrite = brackets(OVERWRITE) + EQUAL + optionallyQuoted(TRUTH)('overwrite')

# Download
download_type = brackets(TYPE) + EQUAL + optionallyQuoted(oneOf('git file svn bzr'))('type')
download_url = brackets(URL) + EQUAL + url
download_hash = brackets(oneOf('md5 sha1 sha256 sha512')('algorithm')) + EQUAL + optionallyQuoted(Word(hexnums))('hash')
download_branch = brackets(BRANCH) + EQUAL + optionallyQuoted(Word(printables))('branch')
download_tag = brackets(TAG) + EQUAL + optionallyQuoted(Word(printables))('tag')
download_revision = brackets(REVISION) + EQUAL + optionallyQuoted(Word(hexnums))('revision')
download_option = download_type | download_url | download_hash | download_branch | download_tag | download_revision
download = (brackets(DOWNLOAD) + download_option)('download')

## Projects ##
# Version
version_number = optionallyQuoted(Combine(Word(nums) + Literal('.') + Word(nums)))('version_number')
version = brackets(VERSION) + EQUAL + version_number

# Type
types = brackets(TYPE) + EQUAL + optionallyQuoted(oneOf('theme module core profile'))('type')

# Project definition
short_version = (EQUAL + version_number)('short_version')
project_options = download | overwrite | patch | subdir | types | version | short_version
name_only = (brackets(empty) + EQUAL + name)('name_only')
projects = (PROJECTS + ((brackets(name) + project_options) | name_only))('projects')

## Libraries ##
# destination
destination = brackets(DESTINATION) + EQUAL + optionallyQuoted(Word(printables))('destination')

# Library definition
libraries_option = download | destination
libraries = (LIBRARIES + brackets(name) + libraries_option)('libraries')

## Grammar ##
statement = (comment | ((api | core | projects | libraries) + Optional(comment)))
grammar = ZeroOrMore(Group(statement)) + stringEnd
