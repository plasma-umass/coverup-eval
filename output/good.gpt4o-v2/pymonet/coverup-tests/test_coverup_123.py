# file: pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.maybe import Maybe

def test_left_to_maybe(monkeypatch):
    from pymonet.either import Left

    # Ensure the Maybe.nothing method is called
    def mock_nothing():
        return "mocked nothing"

    monkeypatch.setattr(Maybe, "nothing", mock_nothing)

    left_instance = Left(value=None)
    maybe_result = left_instance.to_maybe()

    assert maybe_result == "mocked nothing"
