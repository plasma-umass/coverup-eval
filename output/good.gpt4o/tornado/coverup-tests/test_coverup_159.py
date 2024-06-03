# file tornado/util.py:66-73
# lines [66, 67]
# branches []

import pytest
from tornado.util import TimeoutError

def test_timeout_error():
    with pytest.raises(TimeoutError):
        raise TimeoutError("This is a timeout error")

    # Ensure the exception message is correct
    try:
        raise TimeoutError("This is a timeout error")
    except TimeoutError as e:
        assert str(e) == "This is a timeout error"
