from __future__ import with_statement
from makegrammar import destination, ParseException
import pytest


def testSimpleDir():
    line = '[destination] = dir'
    result = destination.parseString(line)
    assert result['destination'] == 'dir'

def testSubDir():
    line = '[destination] = some/dir'
    result = destination.parseString(line)
    assert result['destination'] == 'some/dir'

def testDirNameWithSpaces():
    line = '[destination] = some/long dir'
    with pytest.raises(ParseException):
        destination.parseString(line, True)
