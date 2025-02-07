# file: py_backwards/transformers/dict_unpacking.py:33-44
# asked: {"lines": [33, 35, 36, 37, 38, 39, 41, 42, 44], "branches": [[36, 37], [36, 44], [37, 38], [37, 41]]}
# gained: {"lines": [33, 35, 36, 37, 38, 39, 41, 42, 44], "branches": [[36, 37], [36, 44], [37, 38], [37, 41]]}

import pytest
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Splitted(list):
    pass

@pytest.fixture
def transformer():
    return DictUnpackingTransformer(None)

def test_split_by_None_with_None_key(transformer):
    pairs = [(None, 'value1'), ('key2', 'value2')]
    result = transformer._split_by_None(pairs)
    assert result == [[], 'value1', [('key2', 'value2')]]

def test_split_by_None_without_None_key(transformer):
    pairs = [('key1', 'value1'), ('key2', 'value2')]
    result = transformer._split_by_None(pairs)
    assert result == [[('key1', 'value1'), ('key2', 'value2')]]

def test_split_by_None_mixed(transformer):
    pairs = [('key1', 'value1'), (None, 'value2'), ('key3', 'value3')]
    result = transformer._split_by_None(pairs)
    assert result == [[('key1', 'value1')], 'value2', [('key3', 'value3')]]
