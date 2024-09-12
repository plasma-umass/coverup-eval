# file: pymonet/either.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    
    def test_ap_with_function(self):
        # Mocking the map method
        class MockEither(Either):
            def map(self, value):
                return self.value(value)

        either_instance = Either(5)
        applicative = MockEither(lambda x: x * 2)
        
        result = either_instance.ap(applicative)
        
        assert result == 10  # 5 * 2

    def test_ap_with_non_function(self):
        # Mocking the map method
        class MockEither(Either):
            def map(self, value):
                return self.value

        either_instance = Either(5)
        applicative = MockEither(10)
        
        result = either_instance.ap(applicative)
        
        assert result == 10

    def test_ap_with_exception(self):
        # Mocking the map method to raise an exception
        class MockEither(Either):
            def map(self, value):
                raise ValueError("Test exception")

        either_instance = Either(5)
        applicative = MockEither(lambda x: x * 2)
        
        with pytest.raises(ValueError, match="Test exception"):
            either_instance.ap(applicative)
