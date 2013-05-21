from __future__ import with_statement
from makegrammar import url, ParseException
import pytest


def testUrlCharacters():
    urlchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;/?:@=&$-_.+!*'(),"
    result = url.parseString(urlchars)
    assert result['url'] == urlchars


def testPercentEncoding():
    url_encoded = '%00%aa%AA%af%fa%ff%FF%99'
    result = url.parseString(url_encoded)
    assert result['url'] == url_encoded

def testPercentOnly():
    wrong = '%'
    with pytest.raises(ParseException):
        url.parseString(wrong)

def testWrongPercentEncoding():
    wrong = '%xx'
    with pytest.raises(ParseException):
        url.parseString(wrong)

def testPercentEncodingStarted():
    wrong = '%a'
    with pytest.raises(ParseException):
        url.parseString(wrong)
