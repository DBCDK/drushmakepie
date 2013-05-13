from __future__ import with_statement
from makegrammar import overwrite, ParseException
import pytest


def testOverwriteTrue():
    result = overwrite.parseString('[overwrite] = TRUE')
    assert result['overwrite'] == 'TRUE'

def testOverwriteFalse():
    result = overwrite.parseString('[overwrite] = FALSE')
    assert result['overwrite'] == 'FALSE'

def testOverwriteFail():
    with pytest.raises(ParseException):
        overwrite.parseString('[overwrite] = neither')
