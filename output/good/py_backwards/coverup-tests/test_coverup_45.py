# file py_backwards/transformers/dict_unpacking.py:71-79
# lines [72, 73, 75, 76, 77, 78, 79]
# branches ['72->73', '72->75']

import ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
import pytest

@pytest.fixture
def transformer(mocker):
    mocker.patch.object(DictUnpackingTransformer, '_split_by_None')
    mocker.patch.object(DictUnpackingTransformer, '_prepare_splitted')
    mocker.patch.object(DictUnpackingTransformer, '_merge_dicts')
    return DictUnpackingTransformer(tree=ast.AST())

def test_dict_unpacking_with_none_key(transformer):
    # Create a dict node with None as one of the keys
    dict_node = ast.Dict(keys=[None], values=[ast.Num(n=1)])

    # Visit the dict node with the transformer
    result = transformer.visit_Dict(dict_node)

    # Assertions to ensure the mocked methods were called
    transformer._split_by_None.assert_called_once()
    transformer._prepare_splitted.assert_called_once()
    transformer._merge_dicts.assert_called_once()

    # Assert that the result is the return value of the _merge_dicts method
    assert result == transformer._merge_dicts.return_value
