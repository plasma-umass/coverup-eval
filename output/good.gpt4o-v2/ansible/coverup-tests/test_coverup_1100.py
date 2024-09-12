# file: lib/ansible/module_utils/common/dict_transformations.py:127-154
# asked: {"lines": [137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}
# gained: {"lines": [137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}

import pytest
from ansible.module_utils.common.dict_transformations import recursive_diff
from ansible.module_utils.common._collections_compat import MutableMapping

def test_recursive_diff_type_error():
    with pytest.raises(TypeError, match="Unable to diff 'dict1' .* and 'dict2' .* Both must be a dictionary."):
        recursive_diff([], {})

    with pytest.raises(TypeError, match="Unable to diff 'dict1' .* and 'dict2' .* Both must be a dictionary."):
        recursive_diff({}, [])

def test_recursive_diff_no_diff():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    assert recursive_diff(dict1, dict2) is None

def test_recursive_diff_simple_diff():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 3}
    assert recursive_diff(dict1, dict2) == ({'b': 2}, {'b': 3})

def test_recursive_diff_nested_diff():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 4}}
    dict2 = {'a': 1, 'b': {'c': 3, 'e': 5}}
    assert recursive_diff(dict1, dict2) == (
        {'b': {'c': 2, 'd': 4}},
        {'b': {'c': 3, 'e': 5}}
    )

def test_recursive_diff_left_only():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1}
    assert recursive_diff(dict1, dict2) == ({'b': 2}, {})

def test_recursive_diff_right_only():
    dict1 = {'a': 1}
    dict2 = {'a': 1, 'b': 2}
    assert recursive_diff(dict1, dict2) == ({}, {'b': 2})
