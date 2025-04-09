# file: pymonet/validation.py:16-19
# asked: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}

import pytest
from pymonet.validation import Validation

class TestValidation:
    @pytest.fixture
    def validation_success(self):
        class ValidationSuccess(Validation):
            def __init__(self, value):
                self.value = value
                self.errors = []

        return ValidationSuccess("test_value")

    @pytest.fixture
    def validation_fail(self):
        class ValidationFail(Validation):
            def __init__(self, value, errors):
                self.value = value
                self.errors = errors

        return ValidationFail("test_value", ["error1", "error2"])

    def test_str_success(self, validation_success):
        assert str(validation_success) == "Validation.success[test_value]"

    def test_str_fail(self, validation_fail):
        assert str(validation_fail) == "Validation.fail[test_value, ['error1', 'error2']]"
