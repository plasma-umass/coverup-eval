# file: pymonet/maybe.py:166-177
# asked: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}
# gained: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

class TestMaybe:
    def test_to_validation_with_nothing(self):
        maybe_instance = Maybe(None, True)
        result = maybe_instance.to_validation()
        assert isinstance(result, Validation)
        assert result.value is None
        assert result.errors == []

    def test_to_validation_with_value(self):
        maybe_instance = Maybe('test_value', False)
        result = maybe_instance.to_validation()
        assert isinstance(result, Validation)
        assert result.value == 'test_value'
        assert result.errors == []
