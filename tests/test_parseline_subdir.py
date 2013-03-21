from __future__ import with_statement
import pytest
import drushmake


def testParselineSubdir():
    line = 'projects[my_module][subdir] = some_dir/one-more-dir'
    result = drushmake.parseline(line)
    assert result['projects']['name'] == 'my_module'
    assert result['projects']['subdir'] == 'some_dir/one-more-dir'

def testParselineSubdirSpaces():
    line = 'projects[my_module][subdir] = some_dir/one-more-dir test'
    with pytest.raises(drushmake.ParseException):
        drushmake.parseline(line)
