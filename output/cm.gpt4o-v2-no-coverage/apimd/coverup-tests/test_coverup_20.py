# file: apimd/parser.py:46-48
# asked: {"lines": [46, 48], "branches": []}
# gained: {"lines": [46, 48], "branches": []}

import pytest
from ast import Constant, expr
from apimd.parser import _defaults

def test_defaults_with_values():
    args = [Constant(value=1), Constant(value=2), Constant(value=3)]
    result = list(_defaults(args))
    assert result == ['`1`', '`2`', '`3`']

def test_defaults_with_none():
    args = [None, Constant(value=2), None]
    result = list(_defaults(args))
    assert result == [' ', '`2`', ' ']

def test_defaults_empty():
    args = []
    result = list(_defaults(args))
    assert result == []

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Perform any necessary cleanup after each test
