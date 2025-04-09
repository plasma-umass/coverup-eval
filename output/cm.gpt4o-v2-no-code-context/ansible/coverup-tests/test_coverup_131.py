# file: lib/ansible/template/native_helpers.py:23-43
# asked: {"lines": [23, 27, 28, 29, 30, 31, 32, 34, 41, 43], "branches": [[27, 28], [27, 30], [28, 29], [28, 43], [30, 31], [30, 34], [31, 32], [31, 43], [34, 41], [34, 43]]}
# gained: {"lines": [23, 27, 28, 29, 30, 31, 32, 34, 41, 43], "branches": [[27, 28], [27, 30], [28, 29], [30, 31], [30, 34], [31, 32], [34, 41], [34, 43]]}

import pytest
from unittest.mock import MagicMock
from collections.abc import Mapping

# Assuming the following imports based on the code context
from ansible.template.native_helpers import _fail_on_undefined
from jinja2 import StrictUndefined

class MockMapping(Mapping):
    def __init__(self, *args, **kwargs):
        self.store = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

def test_fail_on_undefined_with_mapping(monkeypatch):
    mock_mapping = MockMapping(a=1, b=StrictUndefined())
    with pytest.raises(Exception):
        _fail_on_undefined(mock_mapping)

def test_fail_on_undefined_with_sequence(monkeypatch):
    mock_sequence = [1, StrictUndefined()]
    with pytest.raises(Exception):
        _fail_on_undefined(mock_sequence)

def test_fail_on_undefined_with_strictundefined(monkeypatch):
    with pytest.raises(Exception):
        _fail_on_undefined(StrictUndefined())

def test_fail_on_undefined_with_other_data():
    data = 42
    result = _fail_on_undefined(data)
    assert result == data
