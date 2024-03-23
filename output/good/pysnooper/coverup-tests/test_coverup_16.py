# file pysnooper/variables.py:53-83
# lines [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83]
# branches ['56->57', '56->67', '58->59', '58->60', '71->exit', '71->72']

import pytest
from pysnooper.variables import CommonVariable
from unittest.mock import MagicMock

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        super().__init__(source)
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _keys(self, main_value):
        return main_value.keys()

    def _format_key(self, key):
        return f".{key}"

    def _get_value(self, main_value, key):
        return main_value[key]

@pytest.fixture
def common_variable():
    return TestCommonVariable('source', 'unambiguous_source', exclude=set())

def test_common_variable_items_with_exception_during_iteration(common_variable):
    class DictWithException(dict):
        def keys(self):
            raise Exception("Test exception during keys")

    main_value = DictWithException(a=1, b=2)
    items = common_variable._items(main_value)
    assert items == [('source', "{'a': 1, 'b': 2}")]

def test_common_variable_items_with_exception_during_value_access(common_variable):
    main_value = {'a': 1, 'b': 2}
    common_variable._get_value = MagicMock(side_effect=Exception("Test exception during value access"))
    items = common_variable._items(main_value)
    assert items == [('source', "{'a': 1, 'b': 2}")]

def test_common_variable_items_with_exclude(common_variable):
    common_variable.exclude.add('b')
    main_value = {'a': 1, 'b': 2}
    items = common_variable._items(main_value)
    assert items == [('source', "{'a': 1, 'b': 2}"), ('unambiguous_source.a', '1')]
