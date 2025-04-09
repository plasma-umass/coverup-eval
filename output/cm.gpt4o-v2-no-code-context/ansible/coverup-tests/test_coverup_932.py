# file: lib/ansible/module_utils/common/dict_transformations.py:127-154
# asked: {"lines": [137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}
# gained: {"lines": [137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154], "branches": [[137, 138], [137, 141], [143, 144], [143, 152], [144, 145], [144, 149], [146, 143], [146, 147], [149, 143], [149, 150], [152, 153], [152, 154]]}

import pytest
from collections.abc import MutableMapping

# Assuming the recursive_diff function is defined in a module named dict_transformations
from ansible.module_utils.common.dict_transformations import recursive_diff

def test_recursive_diff_type_error():
    with pytest.raises(TypeError, match="Unable to diff 'dict1' .* and 'dict2' .* Both must be a dictionary."):
        recursive_diff([], {})

    with pytest.raises(TypeError, match="Unable to diff 'dict1' .* and 'dict2' .* Both must be a dictionary."):
        recursive_diff({}, [])

    with pytest.raises(TypeError, match="Unable to diff 'dict1' .* and 'dict2' .* Both must be a dictionary."):
        recursive_diff([], [])

def test_recursive_diff_no_diff():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    assert recursive_diff(dict1, dict2) is None

def test_recursive_diff_simple_diff():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 3}
    left, right = recursive_diff(dict1, dict2)
    assert left == {'b': 2}
    assert right == {'b': 3}

def test_recursive_diff_nested_diff():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 4}}
    dict2 = {'a': 1, 'b': {'c': 3, 'e': 5}}
    left, right = recursive_diff(dict1, dict2)
    assert left == {'b': {'c': 2, 'd': 4}}
    assert right == {'b': {'c': 3, 'e': 5}}

def test_recursive_diff_additional_keys():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 1, 'b': 2}
    left, right = recursive_diff(dict1, dict2)
    assert left == {'c': 3}
    assert right == {}

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2, 'c': 3}
    left, right = recursive_diff(dict1, dict2)
    assert left == {}
    assert right == {'c': 3}
