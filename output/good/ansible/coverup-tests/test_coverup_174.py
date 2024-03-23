# file lib/ansible/vars/clean.py:22-66
# lines [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66]
# branches ['51->52', '51->54', '54->55', '54->58', '60->61', '60->66', '61->62', '61->64']

import pytest
from ansible.vars.clean import module_response_deepcopy

def test_module_response_deepcopy():
    # Test with a complex nested structure including dicts and lists
    original = {
        'key1': 'value1',
        'key2': [1, 2, {'key3': 'value3'}],
        'key4': {
            'key5': [3, 4, 5],
            'key6': 'value6'
        }
    }
    
    # Perform the deep copy using the custom function
    copied = module_response_deepcopy(original)
    
    # Assert that the copied data is the same as the original
    assert copied == original
    
    # Assert that the dicts are different objects
    assert copied is not original
    assert copied['key4'] is not original['key4']
    
    # Assert that the lists are different objects
    assert copied['key2'] is not original['key2']
    assert copied['key4']['key5'] is not original['key4']['key5']
    
    # Assert that the nested dict is a different object
    assert copied['key2'][2] is not original['key2'][2]
    
    # Test with a non-dict, non-list object
    non_iterable = 'non_iterable'
    assert module_response_deepcopy(non_iterable) == non_iterable

# Note: No cleanup is necessary as the test does not modify any external state
