from unittest import TestCase
import drushmake

class TestDrushmakeParsefile(TestCase):
  def prepareInput(self, file):
    """
    Helper function to parse the single lines.

    Takes an array of text string and sends each through drushmake.parseline()
    """
    z = []
    for line in file:
      z += [drushmake.parseline(line)]
    return z

  def testComments(self):
    """Test various comments."""
    expected = {'drupal': [], 'libraries': [], 'modules': [], 'themes': []}
    simple_comment = self.prepareInput(['# test'])
    no_comment = self.prepareInput(['api = 2', 'core = 7.x'])
    api_core_comment = self.prepareInput(['api = 2', 'core = 7.x', '#test'])
    self.assertEqual(drushmake.parsefile(simple_comment), expected, 'Simple comment.')
    self.assertEqual(drushmake.parsefile(no_comment), expected, 'Only api and core specified.')
    self.assertEqual(drushmake.parsefile(api_core_comment), expected, 'Api, core, and a comment.')

  def testDrupal(self):
    expected = {'drupal': [{'version': '7.17'}],
                'libraries': [],
                'modules': [],
                'themes': []}
    drupal_version_only = self.prepareInput(['api = 2', 'core = 7.x', 'projects[drupal] = 7.17'])
    self.assertEqual(drushmake.parsefile(drupal_version_only), expected, 'Drupal version.')
