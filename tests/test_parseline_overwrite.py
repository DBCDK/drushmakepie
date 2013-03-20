from __future__ import with_statement
import pytest
import drushmake


def testParselineOverwriteTrue():
    result = drushmake.parseline('projects[my_module][overwrite] = TRUE')
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['overwrite'] == 'TRUE'

def testParselineOverwriteFalse():
    result = drushmake.parseline('projects[my_module][overwrite] = FALSE')
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['overwrite'] == 'FALSE'

def testParselineOverwriteFail():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('projects[my_module][overwrite] = neither')
