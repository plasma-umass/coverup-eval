# file: lib/ansible/module_utils/common/dict_transformations.py:127-154
# asked: {"lines": [], "branches": [[146, 143]]}
# gained: {"lines": [], "branches": [[146, 143]]}

import pytest
from ansible.module_utils.common.dict_transformations import recursive_diff
from ansible.module_utils.common._collections_compat import MutableMapping

class TestRecursiveDiff:
    
    def test_recursive_diff_type_error(self):
        with pytest.raises(TypeError):
            recursive_diff([], {})
        with pytest.raises(TypeError):
            recursive_diff({}, [])
        with pytest.raises(TypeError):
            recursive_diff([], [])
    
    def test_recursive_diff_no_diff(self):
        dict1 = {'a': 1, 'b': {'c': 2}}
        dict2 = {'a': 1, 'b': {'c': 2}}
        assert recursive_diff(dict1, dict2) is None
    
    def test_recursive_diff_simple_diff(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 3}
        expected = ({'b': 2}, {'b': 3})
        assert recursive_diff(dict1, dict2) == expected
    
    def test_recursive_diff_nested_diff(self):
        dict1 = {'a': 1, 'b': {'c': 2, 'd': 4}}
        dict2 = {'a': 1, 'b': {'c': 3, 'e': 5}}
        expected = ({'b': {'c': 2, 'd': 4}}, {'b': {'c': 3, 'e': 5}})
        assert recursive_diff(dict1, dict2) == expected
    
    def test_recursive_diff_left_only(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1}
        expected = ({'b': 2}, {})
        assert recursive_diff(dict1, dict2) == expected
    
    def test_recursive_diff_right_only(self):
        dict1 = {'a': 1}
        dict2 = {'a': 1, 'b': 2}
        expected = ({}, {'b': 2})
        assert recursive_diff(dict1, dict2) == expected
