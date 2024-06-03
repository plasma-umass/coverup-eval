# file pymonet/maybe.py:166-177
# lines [166, 173, 175, 176, 177]
# branches ['175->176', '175->177']

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_maybe_to_validation(mocker):
    # Test when Maybe is nothing
    maybe_nothing = Maybe(None, True)
    result = maybe_nothing.to_validation()
    assert isinstance(result, Validation)
    assert result.is_success
    assert result.value is None

    # Test when Maybe has a value
    maybe_value = Maybe(42, False)
    result = maybe_value.to_validation()
    assert isinstance(result, Validation)
    assert result.is_success
    assert result.value == 42
