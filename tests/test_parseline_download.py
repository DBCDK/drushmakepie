from __future__ import with_statement
from makegrammar import download, download_option, ParseException
import pytest


class TestDownloadHash:
    def testBranch(self):
        line = '[download][branch] = develop'
        result = download.parseString(line)
        assert result['download']['branch'] == 'develop'

    def testBranchWithSlash(self):
        line = '[download][branch] = feature/branch'
        result = download.parseString(line)
        assert result['download']['branch'] == 'feature/branch'

    def testMd5(self):
        line = '[download][md5] = 0123456789abcdef'
        result = download.parseString(line)
        assert result['download']['algorithm'] == 'md5'
        assert result['download']['hash'] == '0123456789abcdef'

    def testSha1(self):
        line = '[download][sha1] = 0123456789abcdef'
        result = download.parseString(line)
        assert result['download']['algorithm'] == 'sha1'
        assert result['download']['hash'] == '0123456789abcdef'

    def testSha256(self):
        line = '[download][sha256] = 0123456789abcdef'
        result = download.parseString(line)
        assert result['download']['algorithm'] == 'sha256'
        assert result['download']['hash'] == '0123456789abcdef'

    def testSha512(self):
        line = '[download][sha512] = 0123456789abcdef'
        result = download.parseString(line)
        assert result['download']['algorithm'] == 'sha512'
        assert result['download']['hash'] == '0123456789abcdef'

    def testNotHexString(self):
        line = '[download][sha512] = 0123456789abcdefg'
        with pytest.raises(ParseException):
            download.parseString(line, True)

    def testNotValidAlgorithm(self):
        line = '[download][sha215] = 0123456789abcdef'
        with pytest.raises(ParseException):
            download.parseString(line)

class TestDownloadType:
    def testGit(self):
        line = '[download][type] = git'
        result = download.parseString(line)
        assert result['download']['type'] == 'git'

    def testFile(self):
        line = '[download][type] = file'
        result = download.parseString(line)
        assert result['download']['type'] == 'file'

    def testSvn(self):
        line = '[download][type] = svn'
        result = download.parseString(line)
        assert result['download']['type'] == 'svn'

    def testBzr(self):
        line = '[download][type] = bzr'
        result = download.parseString(line)
        assert result['download']['type'] == 'bzr'

    def testWrongType(self):
        line = '[download][type] = xyz'
        with pytest.raises(ParseException):
            download.parseString(line)

class TestDownloadUrl:
    def testUrl(self):
        line = '[download][url] = git://github.com/DBCDK/drushmakepie.git'
        result = download.parseString(line)
        assert result['download']['url'] == 'git://github.com/DBCDK/drushmakepie.git'

    def testNotValidUrl(self):
        line = '[download][url] = git://github.com/DBCDK/drushmakepie.git space'
        with pytest.raises(ParseException):
            download.parseString(line, True)

class TestDownloadBranch:
    def testSimpleBranchName(self):
        line = '[download][branch] = develop'
        result = download.parseString(line)
        assert result['download']['branch'] == 'develop'

    def testBranchNameWithSlash(self):
        line = '[download][branch] = feature/branch'
        result = download.parseString(line)
        assert result['download']['branch'] == 'feature/branch'

    def testBranchNameWithSpace(self):
        line = '[download][branch] = space in path'
        with pytest.raises(ParseException):
            download.parseString(line, True)

class TestDownloadTag:
    def testSimpleTag(self):
        line = '[download][tag] = named_tag'
        result = download.parseString(line)
        assert result['download']['tag'] == 'named_tag'

    def testVersionTag(self):
        line = '[download][tag] = 7.x-0.2+dbc.1'
        result = download.parseString(line)
        assert result['download']['tag'] == '7.x-0.2+dbc.1'

    def testTabWithSpace(self):
        line = '[download][tag] = space in tag'
        with pytest.raises(ParseException):
            download.parseString(line, True)

class TestDownloadRevision:
    def testRevisionNumber(self):
        line = '[download][revision] = 0123456789abcdef'
        result = download.parseString(line)
        assert result['download']['revision'] == '0123456789abcdef'

    def testIllegalCharacter(self):
        line = '[download][revision] = 0123456789abcdefg'
        with pytest.raises(ParseException):
            download.parseString(line, True)
