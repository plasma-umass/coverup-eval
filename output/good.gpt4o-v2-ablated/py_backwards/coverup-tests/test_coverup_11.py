# file: py_backwards/utils/helpers.py:32-36
# asked: {"lines": [32, 34, 35, 36], "branches": []}
# gained: {"lines": [32, 34, 35, 36], "branches": []}

import pytest
from py_backwards.utils.helpers import get_source
from inspect import getsource
import re

def test_get_source(monkeypatch):
    def mock_getsource(fn):
        return "    def mock_function():\n        pass\n"

    monkeypatch.setattr('py_backwards.utils.helpers.getsource', mock_getsource)

    def sample_function():
        pass

    expected_source = "def mock_function():\n    pass\n"
    actual_source = get_source(sample_function)
    
    assert actual_source == expected_source

