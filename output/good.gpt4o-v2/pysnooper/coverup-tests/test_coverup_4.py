# file: pysnooper/utils.py:90-95
# asked: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest
from pysnooper.utils import ensure_tuple
from pysnooper.pycompat import string_types, collections_abc

def test_ensure_tuple_with_iterable():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)

def test_ensure_tuple_with_string():
    result = ensure_tuple("abc")
    assert result == ("abc",)

def test_ensure_tuple_with_non_iterable():
    result = ensure_tuple(123)
    assert result == (123,)
