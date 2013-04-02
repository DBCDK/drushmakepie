from __future__ import with_statement
import pytest
import drushmake


class TestParselineDownload:
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
