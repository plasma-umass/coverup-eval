# file: pymonet/validation.py:135-144
# asked: {"lines": [135, 142, 144], "branches": []}
# gained: {"lines": [135, 142, 144], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.lazy import Lazy

def test_validation_to_lazy_success():
    validation = Validation.success("test_value")
    lazy_result = validation.to_lazy()
    
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() == "test_value"

def test_validation_to_lazy_failure():
    validation = Validation.fail(["error"])
    lazy_result = validation.to_lazy()
    
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() is None
