# file: pymonet/validation.py:8-14
# asked: {"lines": [8, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 12, 13, 14], "branches": []}

import pytest
from pymonet.validation import Validation

@pytest.fixture
def validation_instance():
    class MockValidation(Validation):
        def __init__(self, value, errors):
            self.value = value
            self.errors = errors
    return MockValidation

def test_validation_equality_same_instance(validation_instance):
    val1 = validation_instance(value=10, errors=[])
    assert val1 == val1

def test_validation_equality_different_instances_same_values(validation_instance):
    val1 = validation_instance(value=10, errors=[])
    val2 = validation_instance(value=10, errors=[])
    assert val1 == val2

def test_validation_equality_different_instances_different_values(validation_instance):
    val1 = validation_instance(value=10, errors=[])
    val2 = validation_instance(value=20, errors=[])
    assert val1 != val2

def test_validation_equality_different_instances_different_errors(validation_instance):
    val1 = validation_instance(value=10, errors=['error1'])
    val2 = validation_instance(value=10, errors=['error2'])
    assert val1 != val2

def test_validation_equality_different_instances_different_types(validation_instance):
    val1 = validation_instance(value=10, errors=[])
    val2 = "Not a Validation instance"
    assert val1 != val2
