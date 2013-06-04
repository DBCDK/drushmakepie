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

def testOverwrite():
    result = projects.parseString('projects[drupal][overwrite] = TRUE')
    assert result['projects']['overwrite'] == 'TRUE'
    assert result['projects']['name'] == 'drupal'

def testDownload():
    result = projects.parseString('projects[drupal][download][type] = git')
    assert result['projects']['download']['type'] == 'git'
    assert result['projects']['name'] == 'drupal'

def testSubdir():
    result = projects.parseString('projects[drupal][subdir] = dir')
    assert result['projects']['subdir'] == 'dir'
    assert result['projects']['name'] == 'drupal'

def testPatch():
    result = projects.parseString('projects[drupal][patch][] = http://example.com/some.patch')
    assert result['projects']['patch']['url'] == 'http://example.com/some.patch'
    assert result['projects']['name'] == 'drupal'

def testTypes():
    result = projects.parseString('projects[drupal][type] = core')
    assert result['projects']['type'] == 'core'
    assert result['projects']['name'] == 'drupal'

def testVersion():
    result = projects.parseString('projects[drupal][version] = 7.17')
    assert result['projects']['version_number'] == '7.17'
    assert result['projects']['name'] == 'drupal'

def testDiretoryName():
    line = 'projects[drupal][directory_name] = directory'
    result = projects.parseString(line)
    assert result['projects']['directory_name'] == 'directory'
    assert result['projects']['name'] == 'drupal'
