# file: py_backwards/utils/snippet.py:102-129
# asked: {"lines": [102, 103, 105, 106, 108, 110, 111, 112, 114, 115, 116, 118, 120, 122, 124, 125, 126, 127, 128, 129], "branches": [[114, 115], [114, 120], [115, 116], [115, 118]]}
# gained: {"lines": [102, 103, 105, 106, 108, 110, 111, 112, 114, 115, 116, 120, 122, 124, 125, 126, 127, 128, 129], "branches": [[114, 115], [114, 120], [115, 116]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import snippet
from py_backwards.utils.helpers import VariablesGenerator, get_source
from py_backwards.utils.tree import find, get_non_exp_parent_and_index, replace_at
from typing import Callable, Dict

# Mock functions and classes
def mock_find_variables(tree: ast.AST):
    return ['x', 'y']

def mock_generate(variable: str) -> str:
    return f'_py_backwards_{variable}_0'

def mock_get_source(fn: Callable[..., None]) -> str:
    return "def test_fn():\n    x = 1\n    y = 2\n"

def mock_extend_tree(tree: ast.AST, variables: Dict[str, str]) -> None:
    pass

class MockVariablesReplacer:
    @classmethod
    def replace(cls, tree: ast.AST, variables: Dict[str, str]) -> ast.AST:
        return tree

@pytest.fixture
def mock_helpers(monkeypatch):
    monkeypatch.setattr('py_backwards.utils.snippet.find_variables', mock_find_variables)
    monkeypatch.setattr(VariablesGenerator, 'generate', mock_generate)
    monkeypatch.setattr('py_backwards.utils.snippet.get_source', mock_get_source)
    monkeypatch.setattr('py_backwards.utils.snippet.extend_tree', mock_extend_tree)
    monkeypatch.setattr('py_backwards.utils.snippet.VariablesReplacer', MockVariablesReplacer)

def test_snippet_init(mock_helpers):
    def test_fn():
        pass
    snip = snippet(test_fn)
    assert snip._fn == test_fn

def test_snippet_get_variables(mock_helpers):
    def test_fn():
        pass
    snip = snippet(test_fn)
    tree = ast.parse("x = 1\ny = 2\n")
    snippet_kwargs = {'x': ast.Name(id='x', ctx=ast.Load())}
    variables = snip._get_variables(tree, snippet_kwargs)
    assert variables == {'x': 'x', 'y': '_py_backwards_y_0'}

def test_snippet_get_body(mock_helpers):
    def test_fn():
        x = 1
        y = 2
    snip = snippet(test_fn)
    body = snip.get_body(x=ast.Name(id='x', ctx=ast.Load()))
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.Assign)
