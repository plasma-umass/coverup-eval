# file: pymonet/either.py:127-136
# asked: {"lines": [127, 134, 136], "branches": []}
# gained: {"lines": [127, 134, 136], "branches": []}

import pytest
from pymonet.either import Left

def test_left_to_maybe(mocker):
    from pymonet.maybe import Maybe

    left_instance = Left("error")
    mocker.patch('pymonet.maybe.Maybe.nothing', return_value="mocked_nothing")

    result = left_instance.to_maybe()

    assert result == "mocked_nothing"
