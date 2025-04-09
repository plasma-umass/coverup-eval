# file: pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest
from pymonet.either import Left

def test_left_to_validation(monkeypatch):
    import pymonet.validation

    class MockValidation:
        @staticmethod
        def fail(value):
            return f"Validation failed with {value}"

    monkeypatch.setattr(pymonet.validation, "Validation", MockValidation)

    left_instance = Left("error_value")
    result = left_instance.to_validation()

    assert result == "Validation failed with ['error_value']"
