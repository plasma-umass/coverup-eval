# file: py_backwards/transformers/return_from_generator.py:64-73
# asked: {"lines": [64, 65, 67, 68, 70, 71, 73], "branches": [[67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [64, 65, 67, 68, 70, 71, 73], "branches": [[67, 68], [67, 70], [70, 71], [70, 73]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

@pytest.fixture
def transformer(mocker):
    tree = mocker.Mock()
    return ReturnFromGeneratorTransformer(tree)

def test_visit_function_def_with_generator_returns(transformer, mocker):
    node = ast.FunctionDef(
        name="test_func",
        args=mocker.Mock(),
        body=[
            ast.Return(value=ast.Constant(value=1)),
            ast.Yield(value=ast.Constant(value=2))
        ],
        decorator_list=[]
    )
    mocker.patch.object(transformer, '_find_generator_returns', return_value=[(node, node.body[0])])
    mocker.patch.object(transformer, '_replace_return')
    mocker.patch.object(transformer, 'generic_visit', return_value=node)

    result = transformer.visit_FunctionDef(node)

    transformer._find_generator_returns.assert_called_once_with(node)
    transformer._replace_return.assert_called_once_with(node, node.body[0])
    transformer.generic_visit.assert_called_once_with(node)
    assert result == node
    assert transformer._tree_changed

def test_visit_function_def_without_generator_returns(transformer, mocker):
    node = ast.FunctionDef(
        name="test_func",
        args=mocker.Mock(),
        body=[
            ast.Return(value=ast.Constant(value=1))
        ],
        decorator_list=[]
    )
    mocker.patch.object(transformer, '_find_generator_returns', return_value=[])
    mocker.patch.object(transformer, '_replace_return')
    mocker.patch.object(transformer, 'generic_visit', return_value=node)

    result = transformer.visit_FunctionDef(node)

    transformer._find_generator_returns.assert_called_once_with(node)
    transformer._replace_return.assert_not_called()
    transformer.generic_visit.assert_called_once_with(node)
    assert result == node
    assert not transformer._tree_changed
