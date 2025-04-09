# file: lib/ansible/vars/clean.py:22-66
# asked: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}
# gained: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}

import pytest
import six
from ansible.vars.clean import module_response_deepcopy

def test_module_response_deepcopy_dict():
    original = {'a': 1, 'b': {'c': 2}}
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
    assert copy['b'] is not original['b']

def test_module_response_deepcopy_list():
    original = [1, [2, 3], 4]
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
    assert copy[1] is not original[1]

def test_module_response_deepcopy_mixed():
    original = {'a': [1, 2, {'b': 3}], 'c': 4}
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
    assert copy['a'] is not original['a']
    assert copy['a'][2] is not original['a'][2]

def test_module_response_deepcopy_non_supported_type():
    original = (1, 2, 3)
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is original
