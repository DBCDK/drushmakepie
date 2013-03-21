from __future__ import with_statement
import pytest
import drushmake


def testParselineTypeTheme():
    result = drushmake.parseline('projects[my_theme][type] = theme')
    assert result['projects']['name'] == 'my_theme'
    assert result['projects']['type'] == 'theme'

def testParselineTypeModule():
    result = drushmake.parseline('projects[my_module][type] = module')
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['type'] == 'module'

def testParselineTypeProfile():
    result = drushmake.parseline('projects[my_profile][type] = profile')
    assert result['projects']['name'] == 'my_profile'
    assert result['projects']['type'] == 'profile'

def testParselineTypeCore():
    result = drushmake.parseline('projects[my_core][type] = core')
    assert result['projects']['name'] == 'my_core'
    assert result['projects']['type'] == 'core'

def testParselineGibberish():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('projects[my_gibberish][type] = gibberish')
