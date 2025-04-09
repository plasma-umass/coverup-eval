# file: py_backwards/transformers/return_from_generator.py:29-54
# asked: {"lines": [29, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 45, 46, 48, 49, 51, 52, 54], "branches": [[35, 36], [35, 51], [38, 39], [38, 40], [40, 41], [40, 42], [42, 43], [42, 45], [45, 46], [45, 48], [48, 35], [48, 49], [51, 52], [51, 54]]}
# gained: {"lines": [29, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 45, 46, 48, 49, 51, 52, 54], "branches": [[35, 36], [35, 51], [38, 39], [38, 40], [40, 41], [40, 42], [42, 45], [45, 46], [45, 48], [48, 35], [48, 49], [51, 52], [51, 54]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

@pytest.fixture
def transformer():
    return ReturnFromGeneratorTransformer(None)

def test_find_generator_returns_with_yield(transformer):
    source = """
def test():
    yield 1
    return 5
"""
    node = ast.parse(source).body[0]
    returns = transformer._find_generator_returns(node)
    assert len(returns) == 1
    assert isinstance(returns[0][1], ast.Return)
    assert returns[0][1].value.n == 5

def test_find_generator_returns_without_yield(transformer):
    source = """
def test():
    return 5
"""
    node = ast.parse(source).body[0]
    returns = transformer._find_generator_returns(node)
    assert len(returns) == 0

def test_find_generator_returns_nested_function(transformer):
    source = """
def test():
    def nested():
        return 5
    yield 1
"""
    node = ast.parse(source).body[0]
    returns = transformer._find_generator_returns(node)
    assert len(returns) == 0

def test_find_generator_returns_with_yield_from(transformer):
    source = """
def test():
    yield from range(5)
    return 5
"""
    node = ast.parse(source).body[0]
    returns = transformer._find_generator_returns(node)
    assert len(returns) == 1
    assert isinstance(returns[0][1], ast.Return)
    assert returns[0][1].value.n == 5
