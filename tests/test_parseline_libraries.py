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

class TestParselineLibrariesUrl:
    def testUrl(self):
        line = 'libraries[my_library][download][url] = http://oss.dbc.dk/public/fake_library.tar.gz'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['url'] == 'http://oss.dbc.dk/public/fake_library.tar.gz'

    def testUrlWithSpaces(self):
        line = 'libraries[my_library][download][url] = http://oss.dbc.dk/public space/fake_library.tar.gz'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineLibrariesType:
    def testGit(self):
        line = 'libraries[my_library][download][type] = git'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['type'] == 'git'

    def testFile(self):
        line = 'libraries[my_library][download][type] = file'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['type'] == 'file'

    def testSvn(self):
        line = 'libraries[my_library][download][type] = svn'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['type'] == 'svn'

    def testBzr(self):
        line = 'libraries[my_library][download][type] = bzr'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['type'] == 'bzr'

    def testXyz(self):
        line = 'libraries[my_library][download][type] = xyz'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)
