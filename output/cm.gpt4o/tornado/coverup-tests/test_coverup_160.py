# file tornado/concurrent.py:42-44
# lines [42, 44]
# branches []

import pytest
from tornado.concurrent import ReturnValueIgnoredError

def test_return_value_ignored_error():
    with pytest.raises(ReturnValueIgnoredError):
        raise ReturnValueIgnoredError("This is a test error")

    # Ensure the exception message is correct
    try:
        raise ReturnValueIgnoredError("This is a test error")
    except ReturnValueIgnoredError as e:
        assert str(e) == "This is a test error"
