# file: pymonet/validation.py:98-109
# asked: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}
# gained: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}

import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

def test_to_either_success():
    validation = Validation.success("value")
    result = validation.to_either()
    assert isinstance(result, Right)
    assert result == Right("value")

def test_to_either_failure():
    validation = Validation.fail(["error"])
    result = validation.to_either()
    assert isinstance(result, Left)
    assert result == Left(["error"])
