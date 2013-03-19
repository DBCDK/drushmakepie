import drushmake


def testApi():
    assert drushmake.parseline('api = 2')['api'] == '2'
    assert drushmake.parseline('api=3')['api'] == '3'
    result = drushmake.parseline('api = 1# comment')
    assert (result['api'], result['comment']) == ('1', 'comment')

