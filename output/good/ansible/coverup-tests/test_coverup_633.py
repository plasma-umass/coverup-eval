# file lib/ansible/parsing/yaml/objects.py:245-248
# lines [245, 246, 247, 248]
# branches ['246->247', '246->248']

import sys
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    ciphertext = "encrypted_data"
    vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    return vault_obj

def test_ansible_vault_encrypted_unicode_find_with_string(vault_encrypted_unicode):
    sub_string = "data"
    start = 0
    end = sys.maxsize
    result = vault_encrypted_unicode.find(sub_string, start, end)
    assert result == vault_encrypted_unicode.data.find(sub_string, start, end)

def test_ansible_vault_encrypted_unicode_find_with_vault(vault_encrypted_unicode):
    sub_vault = AnsibleVaultEncryptedUnicode("data")
    start = 0
    end = sys.maxsize
    result = vault_encrypted_unicode.find(sub_vault, start, end)
    assert result == vault_encrypted_unicode.data.find(sub_vault.data, start, end)
