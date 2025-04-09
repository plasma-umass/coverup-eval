# file: pymonet/validation.py:74-83
# asked: {"lines": [74, 83], "branches": []}
# gained: {"lines": [74, 83], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_bind_success():
    def folder(value):
        return Validation.success(value * 2)

    validation = Validation.success(10)
    result = validation.bind(folder)
    
    assert result.is_success()
    assert result.value == 20

def test_validation_bind_fail():
    def folder(value):
        return Validation.fail(["error"])

    validation = Validation.success(10)
    result = validation.bind(folder)
    
    assert result.is_fail()
    assert result.errors == ["error"]
