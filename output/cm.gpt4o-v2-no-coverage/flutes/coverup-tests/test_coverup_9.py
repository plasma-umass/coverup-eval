# file: flutes/iterator.py:168-197
# asked: {"lines": [168, 187, 188, 189, 190, 191, 193, 194, 195, 196, 197], "branches": [[188, 189], [188, 190], [190, 191], [190, 193], [195, 0], [195, 196]]}
# gained: {"lines": [168, 187, 188, 189, 190, 191, 193, 194, 195, 196, 197], "branches": [[188, 189], [188, 190], [190, 191], [190, 193], [195, 0], [195, 196]]}

import pytest
import operator
from flutes.iterator import scanl

def test_scanl_with_initial_value():
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]

def test_scanl_without_initial_value():
    result = list(scanl(operator.add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

def test_scanl_with_lambda():
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']

def test_scanl_too_many_args():
    with pytest.raises(ValueError, match="Too many arguments"):
        list(scanl(operator.add, [1, 2, 3, 4], 0, 1))
