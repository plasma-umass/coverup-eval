# file: pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest
import re
from pysnooper.utils import normalize_repr

DEFAULT_REPR_RE = re.compile(r'\b0x[0-9a-fA-F]+\b')

def test_normalize_repr_removes_memory_address(monkeypatch):
    def mock_default_repr_re():
        return DEFAULT_REPR_RE
    monkeypatch.setattr('pysnooper.utils.DEFAULT_REPR_RE', mock_default_repr_re())

    item_repr = "<object at 0x7f8b8c8d8e10>"
    expected_repr = "<object at >"
    assert normalize_repr(item_repr) == expected_repr

def test_normalize_repr_no_memory_address(monkeypatch):
    def mock_default_repr_re():
        return DEFAULT_REPR_RE
    monkeypatch.setattr('pysnooper.utils.DEFAULT_REPR_RE', mock_default_repr_re())

    item_repr = "<object at some_location>"
    expected_repr = "<object at some_location>"
    assert normalize_repr(item_repr) == expected_repr

def test_normalize_repr_empty_string(monkeypatch):
    def mock_default_repr_re():
        return DEFAULT_REPR_RE
    monkeypatch.setattr('pysnooper.utils.DEFAULT_REPR_RE', mock_default_repr_re())

    item_repr = ""
    expected_repr = ""
    assert normalize_repr(item_repr) == expected_repr
