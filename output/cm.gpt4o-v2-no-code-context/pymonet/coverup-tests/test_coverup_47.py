# file: pymonet/box.py:103-112
# asked: {"lines": [103, 110, 112], "branches": []}
# gained: {"lines": [103, 110, 112], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_box_to_validation(monkeypatch):
    class MockValidation:
        @staticmethod
        def success(value):
            return f"Validation success with value: {value}"

    monkeypatch.setattr('pymonet.validation.Validation', MockValidation)

    box = Box(42)
    result = box.to_validation()
    
    assert result == "Validation success with value: 42"
