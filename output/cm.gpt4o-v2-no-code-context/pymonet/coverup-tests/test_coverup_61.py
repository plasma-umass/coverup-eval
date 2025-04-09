# file: pymonet/either.py:138-147
# asked: {"lines": [138, 145, 147], "branches": []}
# gained: {"lines": [138], "branches": []}

import pytest
from pymonet.either import Either

def test_left_to_validation(monkeypatch):
    from pymonet.validation import Validation

    class MockValidation:
        @staticmethod
        def fail(value):
            return f"MockValidation.fail called with {value}"

    monkeypatch.setattr(Validation, 'fail', MockValidation.fail)

    class Left(Either):
        def __init__(self, value):
            self.value = value

        def to_validation(self):
            from pymonet.validation import Validation
            return Validation.fail([self.value])

    left_instance = Left("error_value")
    result = left_instance.to_validation()
    assert result == "MockValidation.fail called with ['error_value']"
