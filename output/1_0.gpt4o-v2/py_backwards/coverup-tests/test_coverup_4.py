# file: py_backwards/transformers/formatted_values.py:6-36
# asked: {"lines": [6, 7, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36], "branches": [[18, 19], [18, 21]]}
# gained: {"lines": [6, 7, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36], "branches": [[18, 19], [18, 21]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.formatted_values import FormattedValuesTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return FormattedValuesTransformer(tree)

def test_visit_FormattedValue_with_format_spec(transformer):
    node = ast.FormattedValue(value=ast.Str(s='world'), format_spec=ast.Str(s='.2f'), conversion=-1)
    result = transformer.visit_FormattedValue(node)
    
    assert isinstance(result, ast.Call)
    assert isinstance(result.func, ast.Attribute)
    assert result.func.attr == 'format'
    assert result.func.value.s == '{:.2f}'
    assert len(result.args) == 1
    assert isinstance(result.args[0], ast.Str)
    assert result.args[0].s == 'world'

def test_visit_FormattedValue_without_format_spec(transformer):
    node = ast.FormattedValue(value=ast.Str(s='world'), format_spec=None, conversion=-1)
    result = transformer.visit_FormattedValue(node)
    
    assert isinstance(result, ast.Call)
    assert isinstance(result.func, ast.Attribute)
    assert result.func.attr == 'format'
    assert result.func.value.s == '{}'
    assert len(result.args) == 1
    assert isinstance(result.args[0], ast.Str)
    assert result.args[0].s == 'world'

def test_visit_JoinedStr(transformer):
    node = ast.JoinedStr(values=[ast.Str(s='hello '), ast.FormattedValue(value=ast.Str(s='world'), format_spec=None, conversion=-1)])
    result = transformer.visit_JoinedStr(node)
    
    assert isinstance(result, ast.Call)
    assert isinstance(result.func, ast.Attribute)
    assert result.func.attr == 'join'
    assert result.func.value.s == ''
    assert len(result.args) == 1
    assert isinstance(result.args[0], ast.List)
    assert len(result.args[0].elts) == 2
    assert isinstance(result.args[0].elts[0], ast.Str)
    assert result.args[0].elts[0].s == 'hello '
    assert isinstance(result.args[0].elts[1], ast.Call)
    assert isinstance(result.args[0].elts[1].func, ast.Attribute)
    assert result.args[0].elts[1].func.attr == 'format'
    assert result.args[0].elts[1].func.value.s == '{}'
    assert len(result.args[0].elts[1].args) == 1
    assert isinstance(result.args[0].elts[1].args[0], ast.Str)
    assert result.args[0].elts[1].args[0].s == 'world'
