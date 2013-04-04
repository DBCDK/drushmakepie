from makegrammar import *
import re

class DrushMakeException(Exception):
    pass

def parseline(line):
    def collapsespaces(chars):
        return ' '.join(chars.split())

    if line == '':
        return ()
    else:
        tokens = grammar.parseString(collapsespaces(line))
        return tokens

def parseProject(project):
    name = project['name']
    del project['name']

    if 'version' in project.keys():
        return (name, {'version': project['version']})


def parsefile(lines):
    core = False
    api = False
    tokenized_lines = {'drupal': [], 'libraries': [], 'modules': [], 'themes' : []}

    for line in lines:
        types = line.keys()
        if 'comment' in types:
            pass
        elif 'api' in types:
            api = line['api']
        elif 'core' in types:
            core = line['core']
        elif 'projects' in types:
            (name, part) = parseProject(line['projects'])

            if name == 'drupal':
                tokenized_lines[name] += [part]


    if api != '2':
        for key in tokenized_lines.keys():
            if len(tokenized_lines[key]) > 0:
                raise DrushMakeException('API must be 2!')

    if not core or re.match('^\d+\.x$', core) == None:
        for key in tokenized_lines.keys():
            if len(tokenized_lines[key]) > 0:
                raise DrushMakeException('Core must be of form MAJOR_VERSION.x!')

    return tokenized_lines
