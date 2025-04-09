# file: lib/ansible/vars/clean.py:22-66
# asked: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}
# gained: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}

import pytest
from ansible.vars.clean import module_response_deepcopy

def test_module_response_deepcopy_dict():
    original = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1'}}
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
    assert copy['key2'] is not original['key2']

def test_module_response_deepcopy_list():
    original = ['value1', ['subvalue1', 'subvalue2']]
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
    assert copy[1] is not original[1]

def test_module_response_deepcopy_other():
    original = (1, 2, 3)
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is original

def test_module_response_deepcopy_empty_dict():
    original = {}
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original

def test_module_response_deepcopy_empty_list():
    original = []
    copy = module_response_deepcopy(original)
    assert copy == original
    assert copy is not original
