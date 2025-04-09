# file: pymonet/maybe.py:166-177
# asked: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}
# gained: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_maybe_to_validation_with_value():
    maybe = Maybe.just(10)
    validation = maybe.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success
    assert validation.value == 10

def test_maybe_to_validation_without_value():
    maybe = Maybe.nothing()
    validation = maybe.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success
    assert validation.value is None
