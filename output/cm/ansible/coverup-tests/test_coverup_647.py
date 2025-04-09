# file lib/ansible/parsing/yaml/objects.py:319-322
# lines [319, 320, 321, 322]
# branches ['320->321', '320->322']

import pytest
import sys
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Assuming AnsibleVaultEncryptedUnicode takes a single argument as the encrypted data
    return AnsibleVaultEncryptedUnicode("encrypted_data")

def test_ansible_vault_encrypted_unicode_rfind_with_string(vault_encrypted_unicode):
    assert vault_encrypted_unicode.rfind("data") == 10
    assert vault_encrypted_unicode.rfind("data", 0, 5) == -1

def test_ansible_vault_encrypted_unicode_rfind_with_vault(vault_encrypted_unicode):
    other_vault = AnsibleVaultEncryptedUnicode("data")
    assert vault_encrypted_unicode.rfind(other_vault) == 10
    assert vault_encrypted_unicode.rfind(other_vault, 0, 5) == -1

def test_ansible_vault_encrypted_unicode_rfind_with_not_found(vault_encrypted_unicode):
    assert vault_encrypted_unicode.rfind("not_found") == -1

def test_ansible_vault_encrypted_unicode_rfind_with_empty_string(vault_encrypted_unicode):
    assert vault_encrypted_unicode.rfind("") == len(vault_encrypted_unicode.data)

def test_ansible_vault_encrypted_unicode_rfind_with_maxsize(vault_encrypted_unicode, mocker):
    mocker.patch.object(sys, 'maxsize', 5)
    assert vault_encrypted_unicode.rfind("data", end=sys.maxsize) == -1
