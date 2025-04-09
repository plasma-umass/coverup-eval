# file: apimd/parser.py:513-516
# asked: {"lines": [513, 515, 516], "branches": []}
# gained: {"lines": [513, 515, 516], "branches": []}

import pytest
from ast import parse, Name
from apimd.parser import Parser

def test_parser_resolve(monkeypatch):
    # Mocking the Resolver class
    class MockResolver:
        def __init__(self, root, alias, self_ty):
            self.root = root
            self.alias = alias
            self.self_ty = self_ty

        def visit(self, node):
            return node

        def generic_visit(self, node):
            return node

    monkeypatch.setattr('apimd.parser.Resolver', MockResolver)

    parser = Parser()
    node = parse("x").body[0].value  # Create a simple AST node
    result = parser.resolve("root", node, "self_ty")

    assert result == "x"  # unparse should return the original code

    # Clean up
    monkeypatch.undo()
