# file pymonet/validation.py:8-14
# lines [8, 12, 13, 14]
# branches []

import pytest
from pymonet.validation import Validation

@pytest.fixture
def validation_instance():
    class TestValidation(Validation):
        def __init__(self, value, errors):
            self.value = value
            self.errors = errors

    return TestValidation

def test_validation_equality(validation_instance):
    val1 = validation_instance(value=10, errors=['error1'])
    val2 = validation_instance(value=10, errors=['error1'])
    val3 = validation_instance(value=20, errors=['error2'])
    val4 = validation_instance(value=10, errors=['error2'])
    val5 = validation_instance(value=20, errors=['error1'])

    # Test equality
    assert val1 == val2
    assert val1 != val3
    assert val1 != val4
    assert val1 != val5

    # Test inequality with different types
    assert val1 != "not a validation"
    assert val1 != 10
    assert val1 != None
