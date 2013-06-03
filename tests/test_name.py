from __future__ import with_statement
from makegrammar import name, ParseException
import pytest


def testSimpleName():
    naming = 'name012'
    result = name.parseString(naming)
    assert result['name'] == 'name012'

def testDashedName():
    naming = 'name-123'
    result = name.parseString(naming)
    assert result['name'] == 'name-123'

def testUnderscoredName():
    naming = 'name_123'
    result = name.parseString(naming)
    assert result['name'] == 'name_123'

def testIllegalName():
    naming = '1name'
    with pytest.raises(ParseException):
        name.parseString(naming, True)
