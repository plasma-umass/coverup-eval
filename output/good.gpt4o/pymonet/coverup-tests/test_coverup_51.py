# file pymonet/either.py:17-20
# lines [17, 18, 19, 20]
# branches []

import pytest
from pymonet.either import Either

class TestEither:
    def test_either_eq(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def is_right(self):
                return True

        class Left(Either):
            def __init__(self, value):
                self.value = value

            def is_right(self):
                return False

        right1 = Right(10)
        right2 = Right(10)
        left1 = Left(10)
        left2 = Left(10)
        right3 = Right(20)
        left3 = Left(20)

        # Test equality for Right instances with same value
        assert right1 == right2

        # Test equality for Left instances with same value
        assert left1 == left2

        # Test inequality for Right and Left instances with same value
        assert right1 != left1

        # Test inequality for Right instances with different values
        assert right1 != right3

        # Test inequality for Left instances with different values
        assert left1 != left3

        # Test inequality for Right and Left instances with different values
        assert right1 != left3
        assert left1 != right3
