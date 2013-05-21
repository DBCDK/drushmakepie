from __future__ import with_statement
from makegrammar import projects, ParseException
import pytest


def testNamedOnlyProject():
    result = projects.parseString('projects[] = drupal')
    assert result['projects']['name_only']['name'] == 'drupal'

def testNamedOnlyProjectBracketSpace():
    with pytest.raises(ParseException):
        projects.parseString('projects[ ] = drupal')

def testNamedOnlyProjectSpace():
    with pytest.raises(ParseException):
        projects.parseString('projects [] = drupal')

def testVersionOnlyProject():
    result = projects.parseString('projects[drupal] = 7.17')
    assert result['projects']['short_version']['version_number'] == '7.17'

def testEquivalentProjectOptionOneLevel():
    result = projects.parseString('projects[drupal][overwrite] = TRUE')
    assert result['projects']['overwrite'] == 'TRUE'
    assert result['projects']['name'] == 'drupal'

def testEquivalentProjectOptionTwoLevel():
    result = projects.parseString('projects[drupal][download][type] = git')
    assert result['projects']['download']['type'] == 'git'
    assert result['projects']['name'] == 'drupal'
