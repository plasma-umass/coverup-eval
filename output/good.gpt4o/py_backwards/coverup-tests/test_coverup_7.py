# file py_backwards/transformers/dict_unpacking.py:33-44
# lines [33, 35, 36, 37, 38, 39, 41, 42, 44]
# branches ['36->37', '36->44', '37->38', '37->41']

import pytest
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from typing import List, Tuple, Union

Pair = Tuple[Union[str, None], str]
Splitted = List[Union[List[Pair], str]]

class MockTree:
    pass

@pytest.fixture
def transformer():
    return DictUnpackingTransformer(MockTree())

def test_split_by_None(transformer):
    pairs = [
        ('a', '1'),
        (None, 'unpack1'),
        ('b', '2'),
        ('c', '3'),
        (None, 'unpack2'),
        ('d', '4')
    ]
    
    expected_result = [
        [('a', '1')],
        'unpack1',
        [('b', '2'), ('c', '3')],
        'unpack2',
        [('d', '4')]
    ]
    
    result = transformer._split_by_None(pairs)
    assert result == expected_result
