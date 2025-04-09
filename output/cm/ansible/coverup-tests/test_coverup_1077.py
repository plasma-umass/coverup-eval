# file lib/ansible/parsing/yaml/objects.py:250-251
# lines [250, 251]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_value_{0}_{key}')
    yield encrypted_data
    # Teardown
    # No teardown needed as we are not modifying any external state

def test_ansible_vault_encrypted_unicode_format(vault_encrypted_unicode):
    formatted_data = vault_encrypted_unicode.format(42, key='value')
    assert formatted_data == "encrypted_value_42_value"
