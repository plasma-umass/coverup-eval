# file lib/ansible/parsing/yaml/objects.py:152-153
# lines [152, 153]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('1.23')
    yield vault_str
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_to_float(vault_encrypted_unicode):
    assert float(vault_encrypted_unicode) == 1.23
