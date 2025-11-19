import pytest

@pytest.fixture(scope="module")
def test_suite():
    print('Test suite started')
    yield
    print('Test suite finished')

@pytest.fixture()
def test_case():
    print('Test started')
    yield
    print('Test finished')