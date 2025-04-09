# file lib/ansible/parsing/yaml/objects.py:234-237
# lines [234, 235, 236, 237]
# branches ['235->236', '235->237']

import sys
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def mock_sys_maxsize(mocker):
    mocker.patch.object(sys, 'maxsize', 100)

def test_ansible_vault_encrypted_unicode_count(mock_sys_maxsize):
    # Create an instance of AnsibleVaultEncryptedUnicode with some data
    vault_str = AnsibleVaultEncryptedUnicode('abcabcabc')
    # Create another instance to use as the 'sub' argument
    sub_vault_str = AnsibleVaultEncryptedUnicode('abc')

    # Test the count method with different parameters
    assert vault_str.count(sub_vault_str) == 3
    assert vault_str.count(sub_vault_str, 3) == 2
    assert vault_str.count(sub_vault_str, 3, 7) == 1

    # Test the count method with a regular string as 'sub'
    assert vault_str.count('abc') == 3
    assert vault_str.count('abc', 3) == 2
    assert vault_str.count('abc', 3, 7) == 1

    # Test the count method with a different type that should not be converted
    with pytest.raises(TypeError):
        vault_str.count(123)
