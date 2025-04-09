# file pymonet/either.py:200-209
# lines [200, 207, 209]
# branches []

import pytest
from pymonet.either import Either

class TestRight:
    def test_to_validation(self, mocker):
        from pymonet.validation import Validation

        class Right(Either):
            def to_validation(self):
                from pymonet.validation import Validation
                return Validation.success(self.value)

        right_instance = Right(42)
        validation_result = right_instance.to_validation()

        assert isinstance(validation_result, Validation)
        assert validation_result.is_success()
        assert validation_result.value == 42
