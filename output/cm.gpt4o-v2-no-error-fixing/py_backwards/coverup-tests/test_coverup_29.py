# file: py_backwards/utils/snippet.py:146-157
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest
from py_backwards.utils.snippet import extend

def test_extend_executes(monkeypatch):
    # Mocking the AST assignments
    class MockAST:
        def __init__(self):
            self.assignments = ["x = 1", "x = 2"]

    mock_ast = MockAST()

    # Mocking the extend function to verify it executes
    def mock_extend(var):
        assert var == mock_ast

    monkeypatch.setattr('py_backwards.utils.snippet.extend', mock_extend)

    # Call the function with the mock AST
    extend(mock_ast)
