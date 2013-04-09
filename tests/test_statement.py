from __future__ import with_statement
import pytest
import drushmake


def testSplitLine():
    result = drushmake.parseline("""projects[drupal][version]
        = 7.17""")
    assert result['projects']['name'] == 'drupal'
    assert result['projects']['version'] == '7.17'

def testWrongSplitLine1():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline("""projects
            [drupal][version] = 7.17""")

def testWrongSplitLine2():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline("""projects[drupal]
            [version] = 7.17""")

def testSpaceInBrackets():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline("""projects[ drupal][version] = 7.17""")
