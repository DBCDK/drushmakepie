from __future__ import with_statement
import drushmake
import pytest


def testParselineEmpty():
    assert len(drushmake.parseline('')) == 0 # is None
    assert len(drushmake.parseline(' ')) == 0 # is None

def testGibberish():
    with pytest.raises(drushmake.ParseException):
        assert drushmake.parseline('gibberish')

class TestDrushmakeParse:
    def testEmpty(self):
        result = drushmake.parse('tests/makefiles/empty.make')
        assert len(result) == 0

    def testApiOnly(self):
        result = drushmake.parse('tests/makefiles/apionly.make')
        assert result.api == '2'

    def testCoreOnly(self):
        result = drushmake.parse('tests/makefiles/coreonly.make')
        assert result.core == '7.x'

    def testApiAndCore(self):
        result = drushmake.parse('tests/makefiles/api_core.make')
        assert result.core == '7.x'
        assert result.api == '2'
