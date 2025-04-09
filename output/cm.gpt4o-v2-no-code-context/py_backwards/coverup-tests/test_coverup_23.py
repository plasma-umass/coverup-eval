# file: py_backwards/transformers/return_from_generator.py:64-73
# asked: {"lines": [64, 65, 67, 68, 70, 71, 73], "branches": [[67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [64, 65, 67, 68, 70, 71, 73], "branches": [[67, 68], [67, 70], [70, 71], [70, 73]]}

import ast
import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

class MockTree:
    pass

class TestReturnFromGeneratorTransformer:
    @pytest.fixture
    def transformer(self):
        return ReturnFromGeneratorTransformer(MockTree())

    def test_visit_function_def_with_generator_returns(self, transformer, mocker):
        source = """
def gen():
    yield 1
    return 2
"""
        tree = ast.parse(source)
        func_def = tree.body[0]

        mock_find_generator_returns = mocker.patch.object(
            transformer, '_find_generator_returns', return_value=[(func_def, func_def.body[1])]
        )
        mock_replace_return = mocker.patch.object(transformer, '_replace_return')

        result = transformer.visit_FunctionDef(func_def)

        mock_find_generator_returns.assert_called_once_with(func_def)
        mock_replace_return.assert_called_once_with(func_def, func_def.body[1])
        assert transformer._tree_changed
        assert result is not None

    def test_visit_function_def_without_generator_returns(self, transformer, mocker):
        source = """
def gen():
    yield 1
"""
        tree = ast.parse(source)
        func_def = tree.body[0]

        mock_find_generator_returns = mocker.patch.object(
            transformer, '_find_generator_returns', return_value=[]
        )
        mock_replace_return = mocker.patch.object(transformer, '_replace_return')

        result = transformer.visit_FunctionDef(func_def)

        mock_find_generator_returns.assert_called_once_with(func_def)
        mock_replace_return.assert_not_called()
        assert not transformer._tree_changed
        assert result is not None
