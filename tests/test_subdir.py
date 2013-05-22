from __future__ import with_statement
from makegrammar import subdir, ParseException
import pytest


def testSubdir():
    line = '[subdir] = some_dir/one-more-dir'
    result = subdir.parseString(line)
    assert result['subdir'] == 'some_dir/one-more-dir'

def testSubdirSpaces():
    line = 'projects[my_module][subdir] = some_dir/one-more-dir test'
    with pytest.raises(ParseException):
        subdir.parseString(line)
