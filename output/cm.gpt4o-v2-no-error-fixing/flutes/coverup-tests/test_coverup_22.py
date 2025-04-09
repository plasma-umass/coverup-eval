# file: flutes/iterator.py:69-89
# asked: {"lines": [69, 81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[81, 82], [81, 83], [85, 86], [85, 87]]}
# gained: {"lines": [69, 81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[81, 82], [81, 83], [85, 86], [85, 87]]}

import pytest
from flutes.iterator import drop

def test_drop_with_positive_n():
    result = list(drop(3, range(10)))
    assert result == [3, 4, 5, 6, 7, 8, 9]

def test_drop_with_zero_n():
    result = list(drop(0, range(10)))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_drop_with_negative_n():
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(drop(-1, range(10)))

def test_drop_with_insufficient_elements():
    result = list(drop(10, range(5)))
    assert result == []

def test_drop_with_exact_elements():
    result = list(drop(5, range(5)))
    assert result == []

def test_drop_with_empty_iterable():
    result = list(drop(3, []))
    assert result == []

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: (if needed)
    yield
    # Teardown: (if needed)
    monkeypatch.undo()
