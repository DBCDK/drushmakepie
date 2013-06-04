from __future__ import with_statement
from makegrammar import patch, ParseException
import pytest


def testPatchSimple():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][] = ' + url
    result = patch.parseString(line)
    assert result['patch']['url'] == url

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
    assert result['patch']['url'] == url
    assert result['patch']['patch_name'] == 'pname'

def testPatchUrl():
    url = 'http://someurl.domain/my_patch.diff'
    line = '[patch][pname][url] = ' + url
    result = patch.parseString(line)
    assert result['patch']['patch_name'] == 'pname'
    assert result['patch']['url'] == url

def testPatchChecksum():
    md5 = '0123456789abcdef'
    line = '[patch][pname][md5] = ' + md5
    result = patch.parseString(line)
    assert result['patch']['patch_name'] == 'pname'
    assert result['patch']['md5'] == md5

