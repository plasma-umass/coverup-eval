# file: pymonet/validation.py:111-122
# asked: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

class TestValidation:
    def test_to_maybe_success(self, mocker):
        # Mocking the Validation instance
        validation = mocker.Mock(spec=Validation)
        validation.is_success.return_value = True
        validation.value = "Success Value"

        # Call the method
        result = Validation.to_maybe(validation)

        # Assertions
        assert result == Maybe.just("Success Value")

    def test_to_maybe_failure(self, mocker):
        # Mocking the Validation instance
        validation = mocker.Mock(spec=Validation)
        validation.is_success.return_value = False

        # Call the method
        result = Validation.to_maybe(validation)

        # Assertions
        assert result == Maybe.nothing()
