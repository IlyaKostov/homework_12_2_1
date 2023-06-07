import pytest

from utils import arrs


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    # assert arrs.get([], 0, "test") == "test"
    assert arrs.get(array_fixture, -5, "test") == "test"


def test_get_index_error():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(array_fixture, -2) == [3, 4]
    assert arrs.my_slice(array_fixture, -5) == [1, 2, 3, 4]
