# file py_backwards/transformers/dict_unpacking.py:33-44
# lines [35, 36, 37, 38, 39, 41, 42, 44]
# branches ['36->37', '36->44', '37->38', '37->41']

import pytest
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from ast import parse

@pytest.fixture
def transformer():
    dummy_tree = parse("")
    return DictUnpackingTransformer(tree=dummy_tree)

def test_split_by_None(transformer):
    pairs = [('a', 1), (None, {'b': 2}), ('c', 3)]
    expected_result = [[('a', 1)], {'b': 2}, [('c', 3)]]
    result = transformer._split_by_None(pairs)
    assert result == expected_result
