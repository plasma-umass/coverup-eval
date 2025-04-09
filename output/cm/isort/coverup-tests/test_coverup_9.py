# file isort/exceptions.py:8-9
# lines [8, 9]
# branches []

import pytest
from isort.exceptions import ISortError

def test_isort_error():
    with pytest.raises(ISortError) as exc_info:
        raise ISortError("Test exception for ISortError")

    assert str(exc_info.value) == "Test exception for ISortError", "ISortError did not raise with the correct message"
