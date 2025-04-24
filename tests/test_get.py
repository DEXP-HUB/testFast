import pytest

def get(a, b):
    return a + b


def test_get():
    assert get(2, 2) == 4
