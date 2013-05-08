from __future__ import with_statement # Keyword 'with' not part of python 2.5
from makegrammar import api, ParseException
import pytest


def testApi():
    assert api.parseString('api = 2')['api'] == '2'
    assert api.parseString('api=3')['api'] == '3'
    assert api.parseString('api\n=\n4')['api'] == '4'

def testNotApi():
    with pytest.raises(ParseException):
        api.parseString('api = ')
    with pytest.raises(ParseException):
        api.parseString('api')

