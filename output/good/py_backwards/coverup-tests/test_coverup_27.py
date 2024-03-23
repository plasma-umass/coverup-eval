# file py_backwards/utils/snippet.py:54-56
# lines [54, 55, 56]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

class TestVariablesReplacer:
    @pytest.fixture(autouse=True)
    def setup_method(self, mocker):
        self.replacer = VariablesReplacer(variables={})
        self.mock_replace_field_or_node = mocker.patch.object(self.replacer, '_replace_field_or_node', side_effect=lambda node, name: node)

    def test_visit_ClassDef(self):
        class_node = ast.ClassDef(name='MyClass', bases=[], keywords=[], body=[], decorator_list=[])
        result = self.replacer.visit_ClassDef(class_node)
        assert isinstance(result, ast.ClassDef)
        self.mock_replace_field_or_node.assert_called_once_with(class_node, 'name')
