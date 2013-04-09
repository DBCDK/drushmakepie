from __future__ import with_statement # Keyword 'with' not part of python 2.5
import drushmake
import pytest


def testComment():
    assert drushmake.parseline('#')['comment'] == ''
    assert drushmake.parseline(' #')['comment'] == ''
    assert drushmake.parseline(' # and some text')['comment'] == 'and some text'

def testAlternativeComment():
    assert drushmake.parseline(';')['comment'] == ''
    assert drushmake.parseline(' ;')['comment'] == ''
    assert drushmake.parseline(' ; and some text')['comment'] == 'and some text'

