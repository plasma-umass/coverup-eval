# file: pymonet/either.py:70-79
# asked: {"lines": [70, 77, 79], "branches": []}
# gained: {"lines": [70, 77, 79], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.lazy import Lazy

class TestEither:
    def test_to_lazy(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

        right_instance = Right(42)
        lazy_instance = right_instance.to_lazy()

        assert isinstance(lazy_instance, Lazy)
        assert lazy_instance.get() == 42
