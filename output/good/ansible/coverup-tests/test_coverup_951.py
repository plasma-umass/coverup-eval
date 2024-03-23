# file lib/ansible/utils/unsafe_proxy.py:66-67
# lines [66, 67]
# branches []

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafe

# Test function to check if the AnsibleUnsafe class has the __UNSAFE__ attribute set to True
def test_ansible_unsafe_attribute():
    unsafe_instance = AnsibleUnsafe()
    assert hasattr(unsafe_instance, '__UNSAFE__'), "AnsibleUnsafe object should have the __UNSAFE__ attribute"
    assert unsafe_instance.__UNSAFE__ is True, "The __UNSAFE__ attribute should be True"
