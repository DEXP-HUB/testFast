import pytest



@pytest.fixture(scope='function', autouse=True)
def foo1():
    print('Hello')


@pytest.fixture(scope='function', autouse=True)
def foo2():
    print('World')


class TestFoo:
    def test_foo1(self):
        print('Начало test_foo1')

    def test_foo2(self):
        print('Начала test_foo2')