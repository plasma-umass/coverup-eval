# file tornado/concurrent.py:42-44
# lines [42, 44]
# branches []

import pytest
from tornado.concurrent import ReturnValueIgnoredError

def test_return_value_ignored_error():
    with pytest.raises(ReturnValueIgnoredError) as exc_info:
        raise ReturnValueIgnoredError("This is a test error")

    assert str(exc_info.value) == "This is a test error", "The error message should match the one raised"
