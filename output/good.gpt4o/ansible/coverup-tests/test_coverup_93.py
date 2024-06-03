# file lib/ansible/module_utils/common/dict_transformations.py:127-154
# lines [127, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]
# branches ['137->138', '137->141', '143->144', '143->152', '144->145', '144->149', '146->143', '146->147', '149->143', '149->150', '152->153', '152->154']

import pytest
from collections.abc import MutableMapping
from ansible.module_utils.common.dict_transformations import recursive_diff

def test_recursive_diff_type_error():
    with pytest.raises(TypeError):
        recursive_diff([], {})

    with pytest.raises(TypeError):
        recursive_diff({}, [])

def test_recursive_diff_no_diff():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    assert recursive_diff(dict1, dict2) is None

def test_recursive_diff_simple_diff():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 3}
    expected = ({'b': 2}, {'b': 3})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_nested_diff():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 4}}
    dict2 = {'a': 1, 'b': {'c': 3, 'e': 5}}
    expected = ({'b': {'c': 2, 'd': 4}}, {'b': {'c': 3, 'e': 5}})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_additional_keys():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2, 'c': 3}
    expected = ({}, {'c': 3})
    assert recursive_diff(dict1, dict2) == expected

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 1, 'b': 2}
    expected = ({'c': 3}, {})
    assert recursive_diff(dict1, dict2) == expected

def test_recursive_diff_complex_case():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': {'e': 5}}, 'f': 6}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': {'e': 5}}, 'g': 7}
    expected = ({'b': {'c': 2}, 'f': 6}, {'b': {'c': 3}, 'g': 7})
    assert recursive_diff(dict1, dict2) == expected
