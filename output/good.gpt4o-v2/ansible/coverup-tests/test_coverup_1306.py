# file: lib/ansible/module_utils/common/parameters.py:347-369
# asked: {"lines": [], "branches": [[352, 354]]}
# gained: {"lines": [], "branches": [[352, 354]]}

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from ansible.module_utils.common.text.converters import to_native

def test_return_datastructure_name_with_non_empty_string():
    result = list(_return_datastructure_name("test"))
    assert result == [to_native("test", errors='surrogate_or_strict')]

def test_return_datastructure_name_with_empty_string():
    result = list(_return_datastructure_name(""))
    assert result == []

def test_return_datastructure_name_with_mapping():
    result = list(_return_datastructure_name({"key": "value"}))
    assert result == [to_native("value", errors='surrogate_or_strict')]

def test_return_datastructure_name_with_iterable():
    result = list(_return_datastructure_name(["value1", "value2"]))
    assert result == [to_native("value1", errors='surrogate_or_strict'), to_native("value2", errors='surrogate_or_strict')]

def test_return_datastructure_name_with_bool():
    result = list(_return_datastructure_name(True))
    assert result == []

def test_return_datastructure_name_with_none():
    result = list(_return_datastructure_name(None))
    assert result == []

def test_return_datastructure_name_with_integer():
    result = list(_return_datastructure_name(42))
    assert result == [to_native(42, nonstring='simplerepr')]

def test_return_datastructure_name_with_float():
    result = list(_return_datastructure_name(3.14))
    assert result == [to_native(3.14, nonstring='simplerepr')]

def test_return_datastructure_name_with_unknown_type():
    with pytest.raises(TypeError, match="Unknown parameter type: <class 'complex'>"):
        list(_return_datastructure_name(1+2j))
