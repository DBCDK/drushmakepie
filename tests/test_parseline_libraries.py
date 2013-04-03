from __future__ import with_statement
import pytest
import drushmake


class TestParselineDestination:
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

class TestParselineDownloadUrl:
    def testUrl(self):
        line = 'libraries[my_library][download][url] = http://oss.dbc.dk/public/fake_library.tar.gz'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['url'] == 'http://oss.dbc.dk/public/fake_library.tar.gz'

    def testUrlWithSpaces(self):
        line = 'libraries[my_library][download][url] = http://oss.dbc.dk/public space/fake_library.tar.gz'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadType:
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

class TestParselineDownloadHash:
    def testMd5(self):
        line = 'libraries[my_library][download][md5] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['algorithm'] == 'md5'
        assert result['libraries']['download']['hash'] == '0123456789abcdef'

    def testSha1(self):
        line = 'libraries[my_library][download][sha1] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['algorithm'] == 'sha1'
        assert result['libraries']['download']['hash'] == '0123456789abcdef'

    def testSha256(self):
        line = 'libraries[my_library][download][sha256] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['algorithm'] == 'sha256'
        assert result['libraries']['download']['hash'] == '0123456789abcdef'

    def testSha512(self):
        line = 'libraries[my_library][download][sha512] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['algorithm'] == 'sha512'
        assert result['libraries']['download']['hash'] == '0123456789abcdef'

    def testNotHexString(self):
        line = 'libraries[my_library][download][sha512] = 0123456789abcdefg'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

    def testNotValidAlgorithm(self):
        line = 'libraries[my_library][download][sha215] = 0123456789abcdef'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadBranch:
    def testSimpleBranchName(self):
        line = 'libraries[my_library][download][branch] = develop'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['branch'] == 'develop'

    def testBranchNameWithSlash(self):
        line = 'libraries[my_library][download][branch] = feature/branch'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['branch'] == 'feature/branch'

    def testBranchNameWithSpace(self):
        line = 'libraries[my_library][download][branch] = space in path'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadTag:
    def testSimpleTag(self):
        line = 'libraries[my_library][download][tag] = named_tag'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['tag'] == 'named_tag'

    def testVersionTag(self):
        line = 'libraries[my_library][download][tag] = 7.x-0.2+dbc.1'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['tag'] == '7.x-0.2+dbc.1'

    def testTabWithSpace(self):
        line = 'libraries[my_library][download][tag] = space in tag'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)

class TestParselineDownloadRevision:
    def testRevisionNumber(self):
        line = 'libraries[my_library][download][revision] = 0123456789abcdef'
        result = drushmake.parseline(line)
        assert result['libraries']['name'] == 'my_library'
        assert result['libraries']['download']['revision'] == '0123456789abcdef'

    def testIllegalCharacter(self):
        line = 'libraries[my_library][download][revision] = 0123456789abcdefg'
        with pytest.raises(drushmake.ParseException):
            drushmake.parseline(line)
