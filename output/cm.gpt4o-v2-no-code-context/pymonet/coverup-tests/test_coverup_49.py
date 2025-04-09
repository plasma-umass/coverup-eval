# file: pymonet/either.py:48-57
# asked: {"lines": [48, 55, 57], "branches": []}
# gained: {"lines": [48, 55, 57], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.box import Box

class TestEither:
    def test_to_box(self):
        class MockEither(Either):
            def __init__(self, value):
                self.value = value

        either_instance = MockEither(42)
        box_instance = either_instance.to_box()

        assert isinstance(box_instance, Box)
        assert box_instance.value == 42
