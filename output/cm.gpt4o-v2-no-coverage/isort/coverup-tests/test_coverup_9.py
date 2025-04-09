# file: isort/exceptions.py:108-119
# asked: {"lines": [108, 109, 113, 114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [108, 109, 113, 114, 115, 116, 118, 119], "branches": []}

import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_literal_sort_type_mismatch():
    kind = int
    expected_kind = list
    exception = LiteralSortTypeMismatch(kind, expected_kind)
    
    assert exception.kind == kind
    assert exception.expected_kind == expected_kind
    assert str(exception) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'int'>."
