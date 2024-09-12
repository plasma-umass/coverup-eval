# file: tornado/concurrent.py:42-44
# asked: {"lines": [42, 44], "branches": []}
# gained: {"lines": [42, 44], "branches": []}

import pytest
from tornado.concurrent import ReturnValueIgnoredError

def test_return_value_ignored_error():
    with pytest.raises(ReturnValueIgnoredError):
        raise ReturnValueIgnoredError()

