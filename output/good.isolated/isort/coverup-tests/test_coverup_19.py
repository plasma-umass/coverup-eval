# file isort/exceptions.py:108-119
# lines [108, 109, 113, 114, 115, 116, 118, 119]
# branches []

import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_literal_sort_type_mismatch_exception():
    kind = list
    expected_kind = dict

    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(kind, expected_kind)

    assert str(exc_info.value) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )
    assert exc_info.value.kind == kind
    assert exc_info.value.expected_kind == expected_kind
