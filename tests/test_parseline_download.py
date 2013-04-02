from __future__ import with_statement
import pytest
import drushmake


class TestParselineDownloadHash:
    def testBranch(self):
        line = 'projects[my_module][download][branch] = develop'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['branch'] == 'develop'

    def testBranchWithSlash(self):
        line = 'projects[my_module][download][branch] = feature/branch'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['branch'] == 'feature/branch'

    def testMd5(self):
        line = 'projects[my_module][download][md5] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['algorithm'] == 'md5'
        assert result['projects']['download']['hash'] == '0123456789abcdef'

    def testSha1(self):
        line = 'projects[my_module][download][sha1] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['algorithm'] == 'sha1'
        assert result['projects']['download']['hash'] == '0123456789abcdef'

    def testSha256(self):
        line = 'projects[my_module][download][sha256] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['algorithm'] == 'sha256'
        assert result['projects']['download']['hash'] == '0123456789abcdef'

    def testSha512(self):
        line = 'projects[my_module][download][sha512] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['algorithm'] == 'sha512'
        assert result['projects']['download']['hash'] == '0123456789abcdef'

    def testNotHexString(self):
        line = 'projects[my_module][download][sha512] = 0123456789abcdefg'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

    def testNotValidAlgorithm(self):
        line = 'projects[my_module][download][sha215] = 0123456789abcdef'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadType:
    def testGit(self):
        line = 'projects[my_module][download][type] = git'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['type'] == 'git'

    def testFile(self):
        line = 'projects[my_module][download][type] = file'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['type'] == 'file'

    def testSvn(self):
        line = 'projects[my_module][download][type] = svn'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['type'] == 'svn'

    def testBzr(self):
        line = 'projects[my_module][download][type] = bzr'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['type'] == 'bzr'

    def testWrongType(self):
        line = 'projects[my_module][download][type] = xyz'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadUrl:
    def testUrl(self):
        line = 'projects[my_module][download][url] = git://github.com/DBCDK/drushmakepie.git'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['url'] == 'git://github.com/DBCDK/drushmakepie.git'

    def testNotValidUrl(self):
        line = 'projects[my_module][download][url] = git://github.com/DBCDK/drushmakepie.git space'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadBranch:
    def testSimpleBranchName(self):
        line = 'projects[my_module][download][branch] = develop'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['branch'] == 'develop'

    def testBranchNameWithSlash(self):
        line = 'projects[my_module][download][branch] = feature/branch'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['branch'] == 'feature/branch'

    def testBranchNameWithSpace(self):
        line = 'projects[my_module][download][branch] = space in path'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadTag:
    def testSimpleTag(self):
        line = 'projects[my_module][download][tag] = named_tag'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['tag'] == 'named_tag'

    def testVersionTag(self):
        line = 'projects[my_module][download][tag] = 7.x-0.2+dbc.1'
        result = drushmake.parseline(line)
        assert result['projects']['name'] == 'my_module'
        assert result['projects']['download']['tag'] == '7.x-0.2+dbc.1'

    def testTabWithSpace(self):
        line = 'projects[my_module][download][tag] = space in tag'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)
