from __future__ import with_statement # Keyword 'with' not part of python 2.5
from makegrammar import comment, ParseException
import pytest


def testComment():
    assert comment.parseString('#')['comment'] == ''
    assert comment.parseString(' #')['comment'] == ''
    assert comment.parseString(' # and some text')['comment'] == 'and some text'

def testAlternativeComment():
    assert comment.parseString(';')['comment'] == ''
    assert comment.parseString(' ;')['comment'] == ''
    assert comment.parseString(' ; and some text')['comment'] == 'and some text'

def testNotAComment():
    with pytest.raises(ParseException):
        comment.parseString('no comment')
