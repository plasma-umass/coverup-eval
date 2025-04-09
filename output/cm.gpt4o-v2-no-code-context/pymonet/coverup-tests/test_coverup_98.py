# file: pymonet/validation.py:45-52
# asked: {"lines": [45, 52], "branches": []}
# gained: {"lines": [45, 52], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_is_success_with_no_errors(self):
        validation = Validation(value=None, errors=[])
        assert validation.is_success() is True

    def test_is_success_with_errors(self):
        validation = Validation(value=None, errors=['error1'])
        assert validation.is_success() is False
