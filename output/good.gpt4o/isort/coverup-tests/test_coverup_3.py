# file isort/exceptions.py:8-9
# lines [8, 9]
# branches []

import pytest
from isort.exceptions import ISortError

def test_isort_error():
    with pytest.raises(ISortError) as exc_info:
        raise ISortError("This is a test error")
    
    assert str(exc_info.value) == "This is a test error"
