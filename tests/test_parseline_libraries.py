from __future__ import with_statement
import pytest
import drushmake


class TestParselineLibrariesDestination:
    def testSimpleDir(self):
        line = 'libraries[my_library][destination] = dir'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['destination'] == 'dir'

    def testSubDir(self):
        line = 'libraries[my_library][destination] = some/dir'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['destination'] == 'some/dir'

    def testDirNameWithSpaces(self):
        line = 'libraries[my_library][destination] = some/long dir'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)
