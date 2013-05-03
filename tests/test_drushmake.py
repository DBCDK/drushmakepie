from __future__ import with_statement
import drushmake
import pytest


def testNonStatement():
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('gibberish')
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline('')
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline(' ')

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
