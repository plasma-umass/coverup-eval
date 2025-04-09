# file: lib/ansible/utils/unsafe_proxy.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest

def test_ansible_unsafe_class():
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    # Verify that the class AnsibleUnsafe exists
    assert hasattr(AnsibleUnsafe, '__UNSAFE__')
    # Verify that the __UNSAFE__ attribute is set to True
    assert AnsibleUnsafe.__UNSAFE__ is True
