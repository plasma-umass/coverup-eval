# file: pysnooper/variables.py:53-83
# asked: {"lines": [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83], "branches": [[56, 57], [56, 67], [58, 59], [58, 60], [71, 0], [71, 72]]}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 79, 80, 82, 83], "branches": [[56, 57], [56, 67], [58, 59], [58, 60], [71, 0], [71, 72]]}

import pytest
from pysnooper.variables import CommonVariable, BaseVariable
from pysnooper import utils

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _keys(self, main_value):
        return main_value.keys()

    def _format_key(self, key):
        return f'[{key}]'

    def _get_value(self, main_value, key):
        return main_value[key]

@pytest.fixture
def common_variable():
    return TestCommonVariable(source='source', unambiguous_source='unambiguous_source', exclude=['exclude_key'])

def test_items_with_normal_keys(common_variable):
    main_value = {'key1': 'value1', 'key2': 'value2'}
    result = common_variable._items(main_value)
    assert result == [
        ('source', utils.get_shortish_repr(main_value, normalize=False)),
        ('unambiguous_source[key1]', utils.get_shortish_repr('value1')),
        ('unambiguous_source[key2]', utils.get_shortish_repr('value2'))
    ]

def test_items_with_excluded_key(common_variable):
    main_value = {'key1': 'value1', 'exclude_key': 'value2'}
    result = common_variable._items(main_value)
    assert result == [
        ('source', utils.get_shortish_repr(main_value, normalize=False)),
        ('unambiguous_source[key1]', utils.get_shortish_repr('value1'))
    ]

def test_items_with_exception_in_get_value(common_variable, mocker):
    main_value = {'key1': 'value1', 'key2': 'value2'}
    mocker.patch.object(common_variable, '_get_value', side_effect=lambda mv, k: mv[k] if k == 'key1' else 1/0)
    result = common_variable._items(main_value)
    assert result == [
        ('source', utils.get_shortish_repr(main_value, normalize=False)),
        ('unambiguous_source[key1]', utils.get_shortish_repr('value1'))
    ]

def test_safe_keys_with_exception(common_variable, mocker):
    main_value = {'key1': 'value1', 'key2': 'value2'}
    mocker.patch.object(common_variable, '_keys', side_effect=Exception)
    result = list(common_variable._safe_keys(main_value))
    assert result == []

def test_format_key_not_implemented():
    with pytest.raises(NotImplementedError):
        CommonVariable(source='source')._format_key('key')

def test_get_value_not_implemented():
    with pytest.raises(NotImplementedError):
        CommonVariable(source='source')._get_value('main_value', 'key')
