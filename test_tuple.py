import pytest


@pytest.mark.parametrize('tuple1', [tuple(), (1,), (0, 0)])
def test_len(tuple1):
    assert len(tuple1) >= 0


def test_immutable():
    a = (1, 2, 3)
    try:
        a[0] = 1
    except TypeError:
        print('The tuple is immutable')

def test_string():
    a = tuple('mail.ru')
    assert a == ('m', 'a', 'i', 'l', '.', 'r', 'u')
