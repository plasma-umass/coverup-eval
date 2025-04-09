# file: pysnooper/utils.py:67-78
# asked: {"lines": [71, 72, 75], "branches": [[74, 75]]}
# gained: {"lines": [71, 72, 75], "branches": [[74, 75]]}

import pytest
from pysnooper.utils import get_shortish_repr

def test_get_shortish_repr_with_exception():
    class FaultyRepr:
        def __repr__(self):
            raise ValueError("Intentional error in repr")

    item = FaultyRepr()
    result = get_shortish_repr(item)
    assert result == 'REPR FAILED'

def test_get_shortish_repr_with_normalize(mocker):
    mocker.patch('pysnooper.utils.normalize_repr', return_value='normalized')
    item = "test"
    result = get_shortish_repr(item, normalize=True)
    assert result == 'normalized'

def test_get_shortish_repr_with_max_length(mocker):
    mocker.patch('pysnooper.utils.truncate', return_value='truncated')
    item = "test"
    result = get_shortish_repr(item, max_length=2)
    assert result == 'truncated'
