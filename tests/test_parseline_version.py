import drushmake


def testParselineVesionShort():
    result = drushmake.parseline('projects[drupal] = 7.17')
    assert result['projects']['name'] == 'drupal'
    assert result['projects']['version'] == '7.17'

def testParselineVersionLong():
    result = drushmake.parseline('projects[drupal][version] = 7.17')
    assert result['projects']['name'] == 'drupal'
    assert result['projects']['version'] == '7.17'
