# file: lib/ansible/module_utils/common/dict_transformations.py:127-154
# asked: {"lines": [127, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}
# gained: {"lines": [127, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}

import pytest
from collections.abc import MutableMapping
from ansible.module_utils.common.dict_transformations import recursive_diff

def test_recursive_diff_identical_dicts():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    assert recursive_diff(dict1, dict2) is None

def test_recursive_diff_different_dicts():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 3}}
    expected = ({'b': {'c': 2}}, {'b': {'c': 3}})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_left_extra_key():
    dict1 = {'a': 1, 'b': {'c': 2}, 'd': 4}
    dict2 = {'a': 1, 'b': {'c': 2}}
    expected = ({'d': 4}, {})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_right_extra_key():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}, 'd': 4}
    expected = ({}, {'d': 4})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_type_error():
    with pytest.raises(TypeError):
        recursive_diff({'a': 1}, ['a', 1])

def test_recursive_diff_nested_diff():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 4}}
    dict2 = {'a': 1, 'b': {'c': 3, 'e': 5}}
    expected = ({'b': {'c': 2, 'd': 4}}, {'b': {'c': 3, 'e': 5}})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_empty_dicts():
    dict1 = {}
    dict2 = {}
    assert recursive_diff(dict1, dict2) is None

def test_recursive_diff_one_empty_dict():
    dict1 = {}
    dict2 = {'a': 1}
    expected = ({}, {'a': 1})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_non_dict_types():
    with pytest.raises(TypeError):
        recursive_diff(1, {'a': 1})

    with pytest.raises(TypeError):
        recursive_diff({'a': 1}, 1)
