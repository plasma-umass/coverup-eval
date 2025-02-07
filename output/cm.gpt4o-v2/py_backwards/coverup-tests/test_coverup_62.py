# file: py_backwards/utils/snippet.py:102-129
# asked: {"lines": [110, 111, 112, 114, 115, 116, 118, 120, 124, 125, 126, 127, 128, 129], "branches": [[114, 115], [114, 120], [115, 116], [115, 118]]}
# gained: {"lines": [110, 111, 112, 114, 115, 116, 118, 120, 124, 125, 126, 127, 128, 129], "branches": [[114, 115], [114, 120], [115, 116], [115, 118]]}

import pytest
from unittest.mock import Mock
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import snippet
from py_backwards.utils.helpers import VariablesGenerator, get_source

# Mocking the helper functions and classes
@pytest.fixture
def mock_helpers(monkeypatch):
    mock_find_variables = Mock(return_value=['a', 'b'])
    mock_extend_tree = Mock()
    mock_VariablesReplacer = Mock()
    mock_get_source = Mock(return_value='def fn(): pass')

    monkeypatch.setattr('py_backwards.utils.snippet.find_variables', mock_find_variables)
    monkeypatch.setattr('py_backwards.utils.snippet.extend_tree', mock_extend_tree)
    monkeypatch.setattr('py_backwards.utils.snippet.VariablesReplacer', mock_VariablesReplacer)
    monkeypatch.setattr('py_backwards.utils.snippet.get_source', mock_get_source)

    return mock_find_variables, mock_extend_tree, mock_VariablesReplacer, mock_get_source

def test_get_variables(mock_helpers):
    mock_find_variables, _, _, _ = mock_helpers

    snip = snippet(lambda: None)
    tree = ast.parse("a = 1\nb = 2")
    snippet_kwargs = {'a': ast.Name(id='x', ctx=ast.Load()), 'b': 42}

    variables = snip._get_variables(tree, snippet_kwargs)

    assert variables == {'a': 'x', 'b': 42}
    mock_find_variables.assert_called_once_with(tree)

def test_get_body(mock_helpers):
    _, mock_extend_tree, mock_VariablesReplacer, mock_get_source = mock_helpers

    snip = snippet(lambda: None)
    snippet_kwargs = {'a': ast.Name(id='x', ctx=ast.Load()), 'b': 42}

    body = snip.get_body(**snippet_kwargs)

    assert isinstance(body, list)
    mock_get_source.assert_called_once_with(snip._fn)
    mock_extend_tree.assert_called_once()
    mock_VariablesReplacer.replace.assert_called_once()
