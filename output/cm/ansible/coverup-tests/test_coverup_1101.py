# file lib/ansible/parsing/yaml/objects.py:309-310
# lines [309, 310]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_value')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_partition(vault_encrypted_unicode):
    sep = "_"
    result = vault_encrypted_unicode.partition(sep)
    assert result == ("encrypted", "_", "value"), "The partition method did not return the expected tuple"
