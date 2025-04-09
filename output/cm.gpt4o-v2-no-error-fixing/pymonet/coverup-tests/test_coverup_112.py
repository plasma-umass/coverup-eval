# file: pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest
from pymonet.either import Left
from pymonet.maybe import Maybe

class TestLeft:
    def test_to_maybe(self, mocker):
        mocker.patch('pymonet.maybe.Maybe.nothing', return_value="mocked_nothing")
        
        left_instance = Left("error")
        maybe_instance = left_instance.to_maybe()
        
        assert maybe_instance == "mocked_nothing"
