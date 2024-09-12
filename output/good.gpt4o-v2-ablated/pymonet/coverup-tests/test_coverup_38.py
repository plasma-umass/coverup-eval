# file: pymonet/either.py:200-209
# asked: {"lines": [200, 207, 209], "branches": []}
# gained: {"lines": [200], "branches": []}

import pytest
from pymonet.either import Either

class TestRight:
    def test_to_validation(self, mocker):
        from pymonet.validation import Validation

        class MockRight(Either):
            def __init__(self, value):
                self.value = value

            def to_validation(self):
                from pymonet.validation import Validation
                return Validation.success(self.value)

        mock_value = "test_value"
        right_instance = MockRight(mock_value)
        validation_result = right_instance.to_validation()

        assert isinstance(validation_result, Validation)
        assert validation_result.is_success()
        assert validation_result.value == mock_value
