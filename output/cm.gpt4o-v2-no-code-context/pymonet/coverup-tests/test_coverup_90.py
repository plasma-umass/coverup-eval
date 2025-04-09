# file: pymonet/either.py:81-82
# asked: {"lines": [81, 82], "branches": []}
# gained: {"lines": [81, 82], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_is_right(self, mocker):
        mocker.patch.object(Either, '__init__', lambda self: None)
        either_instance = Either()
        assert either_instance.is_right() is None
