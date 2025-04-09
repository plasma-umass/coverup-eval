# file: pysnooper/variables.py:53-83
# asked: {"lines": [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83], "branches": [[56, 57], [56, 67], [58, 59], [58, 60], [71, 0], [71, 72]]}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 79, 80, 82, 83], "branches": [[56, 57], [56, 67], [58, 59], [58, 60], [71, 0], [71, 72]]}

import pytest
from unittest.mock import MagicMock, patch
from pysnooper.variables import CommonVariable
from pysnooper import utils

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        super().__init__(source, exclude)
        self.unambiguous_source = unambiguous_source

    def _format_key(self, key):
        return f"[{key}]"

    def _get_value(self, main_value, key):
        return main_value[key]

    def _keys(self, main_value):
        return main_value.keys()

@pytest.fixture
def common_variable():
    return TestCommonVariable(source="source", unambiguous_source="unambiguous_source", exclude=["exclude_key"])

def test_items_normal_case(common_variable):
    main_value = {"key1": "value1", "key2": "value2"}
    result = common_variable._items(main_value)
    assert result == [
        ("source", utils.get_shortish_repr(main_value)),
        ("unambiguous_source[key1]", utils.get_shortish_repr("value1")),
        ("unambiguous_source[key2]", utils.get_shortish_repr("value2")),
    ]

def test_items_with_exclude(common_variable):
    main_value = {"key1": "value1", "exclude_key": "value2"}
    result = common_variable._items(main_value)
    assert result == [
        ("source", utils.get_shortish_repr(main_value)),
        ("unambiguous_source[key1]", utils.get_shortish_repr("value1")),
    ]

def test_items_with_exception_in_get_value(common_variable, monkeypatch):
    def mock_get_value(main_value, key):
        if key == "key2":
            raise Exception("Test exception")
        return main_value[key]

    monkeypatch.setattr(common_variable, "_get_value", mock_get_value)
    main_value = {"key1": "value1", "key2": "value2"}
    result = common_variable._items(main_value)
    assert result == [
        ("source", utils.get_shortish_repr(main_value)),
        ("unambiguous_source[key1]", utils.get_shortish_repr("value1")),
    ]

def test_safe_keys_normal_case(common_variable):
    main_value = {"key1": "value1", "key2": "value2"}
    keys = list(common_variable._safe_keys(main_value))
    assert keys == ["key1", "key2"]

def test_safe_keys_with_exception_in_keys(common_variable, monkeypatch):
    def mock_keys(main_value):
        raise Exception("Test exception")

    monkeypatch.setattr(common_variable, "_keys", mock_keys)
    main_value = {"key1": "value1", "key2": "value2"}
    keys = list(common_variable._safe_keys(main_value))
    assert keys == []

def test_keys(common_variable):
    main_value = {"key1": "value1", "key2": "value2"}
    keys = common_variable._keys(main_value)
    assert keys == main_value.keys()

def test_format_key(common_variable):
    with pytest.raises(NotImplementedError):
        CommonVariable("source")._format_key("key")

def test_get_value(common_variable):
    with pytest.raises(NotImplementedError):
        CommonVariable("source")._get_value({"key": "value"}, "key")
