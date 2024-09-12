# file: isort/exceptions.py:8-9
# asked: {"lines": [8, 9], "branches": []}
# gained: {"lines": [8, 9], "branches": []}

import pytest

from isort.exceptions import ISortError

def test_isort_error_inheritance():
    class CustomISortError(ISortError):
        pass

    with pytest.raises(CustomISortError):
        raise CustomISortError("This is a custom isort error")

    with pytest.raises(ISortError):
        raise CustomISortError("This is a custom isort error")

    with pytest.raises(ISortError):
        raise ISortError("This is a base isort error")

    assert issubclass(CustomISortError, ISortError)
    assert isinstance(CustomISortError("error"), ISortError)
