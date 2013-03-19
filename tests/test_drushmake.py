import drushmake


class TestDrushmakeParsefile:
    def prepareInput(self, file):
        """
        Helper function to parse the single lines.

        Takes an array of text string and sends each through
        drushmake.parseline()
        """
        z = []
        for line in file:
            z += [drushmake.parseline(line)]
        return z

    def testComments(self):
        expected = {'drupal': [], 'libraries': [], 'modules': [], 'themes': []}
        simple_comment = self.prepareInput(['# test'])
        no_comment = self.prepareInput(['api = 2', 'core = 7.x'])
        api_core_comment = self.prepareInput(['api = 2', 'core = 7.x', '#test'])
        assert drushmake.parsefile(simple_comment) == expected
        assert drushmake.parsefile(no_comment) == expected
        assert drushmake.parsefile(api_core_comment) == expected

    def testDrupal(self):
        expected = {'drupal': [{'version': '7.17'}],
                    'libraries': [],
                    'modules': [],
                    'themes': []}
        drupal_version_only = self.prepareInput(['api = 2', 'core = 7.x',
            'projects[drupal] = 7.17'])
        assert drushmake.parsefile(drupal_version_only) == expected
