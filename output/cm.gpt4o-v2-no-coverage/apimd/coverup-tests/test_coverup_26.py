# file: apimd/parser.py:518-526
# asked: {"lines": [520, 521, 522, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 522], [521, 523], [525, 520], [525, 526]]}
# gained: {"lines": [520, 521, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 523], [525, 526]]}

import pytest
from types import ModuleType
from unittest.mock import Mock, patch
from apimd.parser import Parser

def test_load_docstring(monkeypatch):
    # Create a mock module with a function that has a docstring
    mock_module = ModuleType("mock_module")
    def mock_function():
        """This is a mock function."""
        pass
    setattr(mock_module, "mock_function", mock_function)

    # Create a Parser instance with a doc that includes the mock function
    parser = Parser()
    parser.doc = {"root.mock_function": ""}

    # Mock the _attr function to return the mock function
    def mock_attr(module, attr):
        return getattr(module, attr)
    monkeypatch.setattr("apimd.parser._attr", mock_attr)

    # Mock the doctest function to return the docstring as-is
    def mock_doctest(doc):
        return doc
    monkeypatch.setattr("apimd.parser.doctest", mock_doctest)

    # Call load_docstring and check the results
    parser.load_docstring("root", mock_module)
    assert parser.docstring["root.mock_function"] == "This is a mock function."
