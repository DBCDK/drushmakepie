from __future__ import with_statement
from makegrammar import core, ParseException
import pytest


def testCore():
    assert core.parseString('core=6.x')['core'] == '6.x'
    assert core.parseString('core = 7.x')['core'] == '7.x'
    assert core.parseString("""core\n= 7.x""")['core'] == '7.x'
    assert core.parseString("""core =\n7.x""")['core'] == '7.x'

def testNotCore():
    with pytest.raises(ParseException):
        core.parseString('core = 7 .x')
    with pytest.raises(ParseException):
        core.parseString('core = 7. x')
