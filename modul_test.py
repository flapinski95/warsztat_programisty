from modul import add_numbers
import pytest

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_numbers_invalid_input():
    with pytest.raises(TypeError):
        add_numbers("abc", 5)
