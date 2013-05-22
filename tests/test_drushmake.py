from __future__ import with_statement
from makegrammar import grammar, ParseException
import pytest


def testNonStatement():
    with pytest.raises(ParseException):
        grammar.parseString('gibberish')

def testEmpty():
    empty = grammar.parseString('')
    assert len(empty) == 0
    blanks = grammar.parseString(' ')
    assert len(blanks) == 0

class TestDrushmakeParse:
    def testEmpty(self):
        result = grammar.parseFile('tests/makefiles/empty.make')
        assert len(result) == 0

    def testApiOnly(self):
        result = grammar.parseFile('tests/makefiles/apionly.make')
        assert result[0].api == '2'

    def testCoreOnly(self):
        result = grammar.parseFile('tests/makefiles/coreonly.make')
        assert result[0].core == '7.x'

    def testApiAndCore(self):
        result = grammar.parseFile('tests/makefiles/api_core.make')
        assert result[0].api == '2'
        assert result[1].core == '7.x'

    def testDoubleCore(self):
        result = grammar.parseFile('tests/makefiles/doublecore.make')
        assert result[0].core == '6.x'
        assert result[1].core == '7.x'

    def testSingleProject(self):
        result = grammar.parseFile('tests/makefiles/single_project.make')
        assert result[0].api == '2'
        assert result[1].core == '7.x'
        assert result[2].projects.name == 'drupal'
        assert result[2].projects.short_version.version_number == '7.22'

    def testItemAppendendProjects(self):
        result = grammar.parseFile('tests/makefiles/item_appended_projects.make')
        assert result[0].api == '2'
        assert result[1].core == '7.x'
        assert result[2].projects.name_only.name == 'drupal'
