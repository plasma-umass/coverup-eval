# file pymonet/maybe.py:166-177
# lines [166, 173, 175, 176, 177]
# branches ['175->176', '175->177']

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_maybe_to_validation_success_with_value():
    maybe_with_value = Maybe.just(10)
    validation_result = maybe_with_value.to_validation()
    assert isinstance(validation_result, Validation)
    assert validation_result.is_success
    assert validation_result.value == 10

def test_maybe_to_validation_success_with_none():
    maybe_without_value = Maybe.nothing()
    validation_result = maybe_without_value.to_validation()
    assert isinstance(validation_result, Validation)
    assert validation_result.is_success
    assert validation_result.value is None
