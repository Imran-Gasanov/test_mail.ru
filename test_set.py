import pytest


@pytest.mark.parametrize('set1', [set('a'), set('aaa'), {'a', 'a', 'a', 'a'}])
def test_len(set1):
    assert set1 == {'a'}


def test_add():
    a = {'Hello'}
    a.add('World')
    assert a == {'Hello', 'World'}


def test_remove():
    a = {1, 2, 3}
    try:
        a.remove(4)
    except KeyError:
        print('no such element exists')
