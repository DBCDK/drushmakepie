from __future__ import with_statement
import pytest
import drushmake


def testParselineCore():
    assert drushmake.parseline('core = 7.x')['core'] == '7.x'
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('core = 7 .x')['core']
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('core = 7. x')['core'] 
