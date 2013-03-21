from __future__ import with_statement
import pytest
import drushmake


def testParselinePatchSimple():
    url = 'http://someurl.domain/my_patch.diff'
    line = 'projects[my_module][patch][] = ' + url
    result = drushmake.parseline(line)
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['url'] == url

def testParselinePatchMissingBrackets():
    url = 'http://someurl.domain/my_patch.diff'
    line = 'projects[my_module][patch] = ' + url
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline(line)

def testParselinePatchUrlSpaces():
    url = 'http://someurl.domain/my_patch.diff no spaces'
    line = 'projects[my_module][patch] = ' + url
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline(line)

def testParselinePatchNamed():
    url = 'http://someurl.domain/my_patch.diff'
    line = 'projects[my_module][patch][pname] = ' + url
    result = drushmake.parseline(line)
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['url'] == url
    assert result['projects']['patch'] == 'pname'

def testParselinePatchChecksum():
    md5 = '0123456789abcdef'
    url = 'http://someurl.domain/my_patch.diff'
    line = 'projects[my_module][patch][pname][md5] = ' + md5
    result = drushmake.parseline(line)
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['patch'] == 'pname'
    assert result['projects']['md5'] == md5

