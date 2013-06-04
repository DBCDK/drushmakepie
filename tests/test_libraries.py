from __future__ import with_statement
from makegrammar import libraries, ParseException
import pytest


def testDestination():
    line = 'libraries[my_library][destination] = dir'
    result = libraries.parseString(line)
    assert result['libraries']['name'] == 'my_library'
    assert result['libraries']['destination'] == 'dir'

def testDownload():
    line = 'libraries[my_library][download][url] = http://oss.dbc.dk/public/fake_library.tar.gz'
    result = libraries.parseString(line)
    assert result['libraries']['name'] == 'my_library'
    assert result['libraries']['download']['url'] == 'http://oss.dbc.dk/public/fake_library.tar.gz'

def testPatch():
    line = 'libraries[my_library][patch][] = http://oss.dbc.dk/public/fake_library.patch'
    result = libraries.parseString(line)
    assert result['libraries']['name'] == 'my_library'
    assert result['libraries']['patch']['url'] == 'http://oss.dbc.dk/public/fake_library.patch'

def testDiretoryName():
    line = 'libraries[my_library][directory_name] = directory'
    result = libraries.parseString(line)
    assert result['libraries']['directory_name'] == 'directory'
    assert result['libraries']['name'] == 'my_library'
