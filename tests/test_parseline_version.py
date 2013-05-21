from __future__ import with_statement
from makegrammar import version, version_number, ParseException
import pytest


def testVersionNumber():
    result = version_number.parseString('7.17')
    assert result['version_number'] == '7.17'

def testMissingMajorVersion():
    with pytest.raises(ParseException):
        version_number.parseString('.17')

def testMissingMinorVersion():
    with pytest.raises(ParseException):
        version_number.parseString('7.')

def testSpacedVersion():
    with pytest.raises(ParseException):
        version_number.parseString('7 .17')

def testVersionLong():
    result = version.parseString('[version] = 7.17')
    assert result['version_number'] == '7.17'
