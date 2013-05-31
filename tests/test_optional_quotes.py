from __future__ import with_statement
from makegrammar import optionallyQuoted, url, ParseException
from pyparsing import *
import pytest

def testQoutedNums():
    numbers = '0123456789'
    qnums = optionallyQuoted(Word(nums))
    single_quoted = "'" + numbers + "'"
    double_quoted = '"' + numbers + '"'
    assert qnums.parseString(numbers)[0] == numbers
    assert qnums.parseString(single_quoted)[0] == numbers
    assert qnums.parseString(double_quoted)[0] == numbers
    with pytest.raises(ParseException):
        qnums.parseString('abc012', True)

def testQuotedHexnums():
    hexnumbers = '0123456789abcdef'
    qhexnums = optionallyQuoted(Word(hexnums))
    single_quoted = "'" + hexnumbers + "'"
    double_quoted = '"' + hexnumbers + '"'
    assert qhexnums.parseString(hexnumbers)[0] == hexnumbers
    assert qhexnums.parseString(single_quoted)[0] == hexnumbers
    assert qhexnums.parseString(double_quoted)[0] == hexnumbers
    with pytest.raises(ParseException):
        qhexnums.parseString('ga0b32', True)

def testQoutedAlphanums():
    andu = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    qandu = optionallyQuoted(Word(andu))
    single_quoted = "'" + andu + "'"
    double_quoted = '"' + andu + '"'
    assert qandu.parseString(andu)[0] == andu
    assert qandu.parseString(single_quoted)[0] == andu
    assert qandu.parseString(double_quoted)[0] == andu
    with pytest.raises(ParseException):
        qandu.parseString('+abc012', True)

def testQuotedUrl():
    urlchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;/?:@=&$-_.+!*'(),"
    assert url.parseString(urlchars)['url'] == urlchars
    assert url.parseString("'" + urlchars.replace("'", "\\'") + "'")['url'] == urlchars
    assert url.parseString('"' + urlchars + '"')['url'] == urlchars
    with pytest.raises(ParseException):
        url.parseString("'" + urlchars, True)

def testMultipleApostrophsEmbedded():
    urlchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;/?:@=&$-_.+!*'(),"
    modded = urlchars.replace('b', "'")
    assert url.parseString(modded)[0] == modded

def testUnmatchedStartingSingleQuote():
    urlchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;/?:@=&$-_.+!*'(),"
    modded = "'" + urlchars.replace("'", "")
    assert url.parseString(modded)[0] == modded
