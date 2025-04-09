# file: pymonet/validation.py:111-122
# asked: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

class TestValidation:
    @pytest.fixture
    def validation_success(self):
        class ValidationSuccess(Validation):
            def __init__(self, value):
                self.value = value
                self.errors = []

            def is_success(self):
                return len(self.errors) == 0

        return ValidationSuccess("success_value")

    @pytest.fixture
    def validation_failure(self):
        class ValidationFailure(Validation):
            def __init__(self):
                self.errors = ["error"]

            def is_success(self):
                return len(self.errors) == 0

        return ValidationFailure()

    def test_to_maybe_success(self, validation_success):
        result = validation_success.to_maybe()
        assert result == Maybe.just("success_value")

    def test_to_maybe_failure(self, validation_failure):
        result = validation_failure.to_maybe()
        assert result == Maybe.nothing()
