# file lib/ansible/module_utils/common/dict_transformations.py:127-154
# lines [127, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]
# branches ['137->138', '137->141', '143->144', '143->152', '144->145', '144->149', '146->143', '146->147', '149->143', '149->150', '152->153', '152->154']

import pytest
from collections.abc import MutableMapping
from ansible.module_utils.common.dict_transformations import recursive_diff

def test_recursive_diff():
    # Test with nested dictionaries
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': 3}}
    expected_left = {'b': {'c': 2}}
    expected_right = {'b': {'c': 3}}
    assert recursive_diff(dict1, dict2) == (expected_left, expected_right)

    # Test with no differences
    assert recursive_diff(dict1, dict1) is None

    # Test with different types
    with pytest.raises(TypeError):
        recursive_diff(dict1, "not a dict")

    # Test with one key missing in second dict
    dict3 = {'a': 1, 'b': 2}
    dict4 = {'a': 1}
    expected_left = {'b': 2}
    expected_right = {}
    assert recursive_diff(dict3, dict4) == (expected_left, expected_right)

    # Test with one key missing in first dict
    assert recursive_diff(dict4, dict3) == (expected_right, expected_left)

    # Test with completely different keys
    dict5 = {'e': 5}
    dict6 = {'f': 6}
    expected_left = {'e': 5}
    expected_right = {'f': 6}
    assert recursive_diff(dict5, dict6) == (expected_left, expected_right)

# Ensure the test does not run on import
if __name__ == "__main__":
    pytest.main()
