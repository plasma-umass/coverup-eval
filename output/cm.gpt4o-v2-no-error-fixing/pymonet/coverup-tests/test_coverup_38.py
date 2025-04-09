# file: pymonet/validation.py:16-19
# asked: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}

import pytest
from pymonet.validation import Validation

def test_validation_str_success():
    validation = Validation(value="test_value", errors=[])
    assert str(validation) == "Validation.success[test_value]"

def test_validation_str_fail():
    validation = Validation(value="test_value", errors=["error1", "error2"])
    assert str(validation) == "Validation.fail[test_value, ['error1', 'error2']]"
