# file lib/ansible/parsing/yaml/objects.py:213-214
# lines [213, 214]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    return AnsibleVaultEncryptedUnicode('encrypted_data')

def test_ansible_vault_encrypted_unicode_multiplication(vault_encrypted_unicode):
    multiplied_data = vault_encrypted_unicode * 3
    assert multiplied_data == 'encrypted_dataencrypted_dataencrypted_data'
