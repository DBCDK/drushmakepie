from __future__ import with_statement
from makegrammar import types, ParseException
import pytest


def testTypeTheme():
    result = types.parseString('[type] = theme')
    assert result['type'] == 'theme'

def testTypeModule():
    result = types.parseString('[type] = module')
    assert result['type'] == 'module'

def testTypeProfile():
    result = types.parseString('[type] = profile')
    assert result['type'] == 'profile'

def testTypeCore():
    result = types.parseString('[type] = core')
    assert result['type'] == 'core'

def testGibberish():
    with pytest.raises(ParseException):
        types.parseString('[type] = gibberish')
