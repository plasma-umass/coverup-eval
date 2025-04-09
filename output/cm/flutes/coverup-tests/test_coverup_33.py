# file flutes/iterator.py:168-197
# lines [168, 187, 188, 189, 190, 191, 193, 194, 195, 196, 197]
# branches ['188->189', '188->190', '190->191', '190->193', '195->exit', '195->196']

import pytest
from flutes.iterator import scanl

def test_scanl_with_initial_value():
    # Test scanl with an initial value
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]

def test_scanl_without_initial_value():
    # Test scanl without an initial value
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

def test_scanl_with_too_many_arguments():
    # Test scanl with too many arguments, expecting a ValueError
    with pytest.raises(ValueError):
        list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], 0, 1))

def test_scanl_with_empty_iterable_and_initial_value():
    # Test scanl with an empty iterable and an initial value
    result = list(scanl(lambda acc, x: acc + x, [], 0))
    assert result == [0]

def test_scanl_with_empty_iterable_without_initial_value():
    # Test scanl with an empty iterable without an initial value
    # This should return a list with the first element of the iterable, which is None
    result = list(scanl(lambda acc, x: acc + x, iter([None])))
    assert result == [None]
