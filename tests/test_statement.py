from __future__ import with_statement
from makegrammar import statement, ParseException
import pytest


def testSplitLine():
    result = statement.parseString("""projects[drupal][version]
        = 7.17""")
    assert result['projects']['name'] == 'drupal'
    assert result['projects']['version_number'] == '7.17'

def testWrongSplitLine1():
    with pytest.raises(ParseException):
        statement.parseString("""projects
            [drupal][version] = 7.17""")

def testWrongSplitLine2():
    with pytest.raises(ParseException):
        statement.parseString("""projects[drupal]
            [version] = 7.17""")

def testSpaceInBrackets():
    with pytest.raises(ParseException):
        statement.parseString("""projects[ drupal][version] = 7.17""")

def testMatchComment():
    result = statement.parseString(""" # this is a comment""")
    assert result['comment'] == 'this is a comment'

def testMatchStatementWithComment():
    result = statement.parseString(""" api = 2 # this is a comment""")
    assert result['comment'] == 'this is a comment'
