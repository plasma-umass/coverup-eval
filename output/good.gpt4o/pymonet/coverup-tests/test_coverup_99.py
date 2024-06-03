# file pymonet/validation.py:54-61
# lines [54, 61]
# branches []

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_is_fail_with_errors(self):
        validation = Validation(value=None, errors=['error1', 'error2'])
        assert validation.is_fail() is True

    def test_is_fail_without_errors(self):
        validation = Validation(value=None, errors=[])
        assert validation.is_fail() is False
