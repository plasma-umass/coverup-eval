# file lib/ansible/vars/clean.py:69-95
# lines [77, 78, 79, 87, 88, 91, 93]
# branches ['72->75', '75->77', '77->78', '77->95', '78->77', '78->79', '81->93', '85->90', '86->87', '90->91']

import pytest
from collections.abc import MutableMapping, MutableSequence
from ansible.errors import AnsibleError

# Assuming the strip_internal_keys function is imported from the ansible.vars.clean module
from ansible.vars.clean import strip_internal_keys

def test_strip_internal_keys_full_coverage(mocker):
    # Test to cover lines 77-79
    nested_list = [{'_ansible_key': 'value'}, ['_ansible_key2']]
    strip_internal_keys(nested_list)
    assert nested_list == [{}, ['_ansible_key2']]

    # Test to cover lines 87-88
    dirty_dict_with_exception = {'_ansible_key': 'value', 'key': 'value'}
    strip_internal_keys(dirty_dict_with_exception, exceptions=('_ansible_key',))
    assert dirty_dict_with_exception == {'_ansible_key': 'value', 'key': 'value'}

    # Test to cover lines 91-93
    with pytest.raises(AnsibleError):
        strip_internal_keys('not a mutable sequence or mapping')

    # Test to cover branches 72->75 and 85->90
    dirty_dict_with_nested = {'_ansible_key': 'value', 'nested': {'_ansible_nested_key': 'value'}}
    strip_internal_keys(dirty_dict_with_nested)
    assert dirty_dict_with_nested == {'nested': {}}

# Note: The actual test function name should be unique and descriptive according to the test being performed.
# The above test function name is generic and should be replaced with a more descriptive one.
