# file: pymonet/validation.py:8-14
# asked: {"lines": [8, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 12, 13, 14], "branches": []}

import pytest
from pymonet.validation import Validation

@pytest.fixture
def validation_instance():
    return Validation(value=42, errors=[])

@pytest.fixture
def another_validation_instance():
    return Validation(value=42, errors=[])

def test_validation_equality_same_instance(validation_instance):
    assert validation_instance == validation_instance

def test_validation_equality_different_instance_same_values(validation_instance, another_validation_instance):
    assert validation_instance == another_validation_instance

def test_validation_inequality_different_errors():
    validation1 = Validation(value=42, errors=['error1'])
    validation2 = Validation(value=42, errors=['error2'])
    assert validation1 != validation2

def test_validation_inequality_different_values():
    validation1 = Validation(value=42, errors=[])
    validation2 = Validation(value=43, errors=[])
    assert validation1 != validation2

def test_validation_inequality_different_type(validation_instance):
    assert validation_instance != "not a validation instance"
