# file: sty/primitive.py:202-206
# asked: {"lines": [202, 206], "branches": []}
# gained: {"lines": [202, 206], "branches": []}

import pytest
from sty.primitive import Register
from copy import deepcopy

def test_register_copy(monkeypatch):
    # Create a mock for deepcopy to ensure it is called correctly
    def mock_deepcopy(obj):
        return "deepcopied"

    monkeypatch.setattr("sty.primitive.deepcopy", mock_deepcopy)

    reg = Register()
    copied_reg = reg.copy()

    assert copied_reg == "deepcopied"
