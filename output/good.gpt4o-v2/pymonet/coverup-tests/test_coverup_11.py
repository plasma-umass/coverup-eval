# file: pymonet/validation.py:98-109
# asked: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}
# gained: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}

import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

def test_validation_to_either_success():
    validation = Validation.success("test_value")
    result = validation.to_either()
    assert isinstance(result, Right)
    assert result == Right("test_value")

def test_validation_to_either_failure():
    validation = Validation.fail(["error1", "error2"])
    result = validation.to_either()
    assert isinstance(result, Left)
    assert result == Left(["error1", "error2"])
