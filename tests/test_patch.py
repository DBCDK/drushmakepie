from __future__ import with_statement
from makegrammar import patch, ParseException
import pytest


def testPatchSimple():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][] = ' + url
    result = patch.parseString(line)
    assert result['url'] == url

def testPatchMissingBrackets():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch] = ' + url
    with pytest.raises(ParseException):
        patch.parseString(line)

def testPatchUrlSpaces():
    url = 'http://someurl.domain/my_patch.diff no spaces'
    line = '[patch] = ' + url
    with pytest.raises(ParseException):
        patch.parseString(line)

def testPatchNamed():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][pname] = ' + url
    result = patch.parseString(line)
    assert result['url'] == url
    assert result['patch'] == 'pname'

def testPatchUrl():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][pname][url] = ' + url
    result = patch.parseString(line)
    assert result['patch'] == 'pname'
    assert result['url'] == url

def testPatchChecksum():
    md5 = '0123456789abcdef'
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][pname][md5] = ' + md5
    result = patch.parseString(line)
    assert result['patch'] == 'pname'
    assert result['md5'] == md5

