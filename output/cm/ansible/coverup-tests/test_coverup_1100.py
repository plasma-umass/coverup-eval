# file lib/ansible/parsing/yaml/objects.py:345-346
# lines [345, 346]
# branches []

import pytest
import sys
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Assuming the correct initialization of AnsibleVaultEncryptedUnicode without 'data' keyword
    return AnsibleVaultEncryptedUnicode("!vault |$ANSIBLE_VAULT;1.1;AES256\n          303132333435363738")

def test_ansible_vault_encrypted_unicode_startswith(vault_encrypted_unicode):
    assert vault_encrypted_unicode.startswith('!vault') == True
    assert vault_encrypted_unicode.startswith('!valt') == False
    assert vault_encrypted_unicode.startswith('!vault', 0, 10) == True
    assert vault_encrypted_unicode.startswith('!vault', 0, 2) == False
    assert vault_encrypted_unicode.startswith('!vault', 0, sys.maxsize) == True
