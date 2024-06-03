# file pymonet/either.py:138-147
# lines [138, 145, 147]
# branches []

import pytest
from pymonet.either import Either

class TestLeft:
    def test_to_validation(self, mocker):
        from pymonet.validation import Validation

        class MockLeft(Either):
            def __init__(self, value):
                self.value = value

            def to_validation(self):
                from pymonet.validation import Validation
                return Validation.fail([self.value])

        left_instance = MockLeft("error_value")
        validation_result = left_instance.to_validation()

        assert isinstance(validation_result, Validation)
        assert validation_result.is_fail()
        assert validation_result.errors == ["error_value"]
