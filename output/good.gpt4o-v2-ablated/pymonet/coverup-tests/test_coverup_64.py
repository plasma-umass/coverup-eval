# file: pymonet/validation.py:63-72
# asked: {"lines": [63, 72], "branches": []}
# gained: {"lines": [63, 72], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_map_success(self):
        validation = Validation(10, [])
        result = validation.map(lambda x: x * 2)
        assert result.value == 20
        assert result.errors == []

    def test_map_with_errors(self):
        validation = Validation(10, ['error1'])
        result = validation.map(lambda x: x * 2)
        assert result.value == 20
        assert result.errors == ['error1']

    def test_map_with_different_mapper(self):
        validation = Validation("test", [])
        result = validation.map(lambda x: x.upper())
        assert result.value == "TEST"
        assert result.errors == []

    def test_map_with_errors_and_different_mapper(self):
        validation = Validation("test", ['error1'])
        result = validation.map(lambda x: x.upper())
        assert result.value == "TEST"
        assert result.errors == ['error1']
