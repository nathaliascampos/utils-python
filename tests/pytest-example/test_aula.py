import pytest


def soma_1(num):
    return int(num) + 1


def test_soma_1():
    assert soma_1(41) == 42


def test_soma_1_num_as_str():
    assert soma_1("41") == 42


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1('fabio')
