# file: pymonet/validation.py:146-155
# asked: {"lines": [146, 153, 155], "branches": []}
# gained: {"lines": [146, 153, 155], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

def test_validation_to_try_success():
    validation = Validation.success("test_value")
    result = validation.to_try()
    
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == "test_value"

def test_validation_to_try_failure():
    validation = Validation.fail(["error"])
    result = validation.to_try()
    
    assert isinstance(result, Try)
    assert not result.is_success
    assert result.value is None
