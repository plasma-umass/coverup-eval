# file lib/ansible/parsing/yaml/objects.py:339-340
# lines [339, 340]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_value')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_rsplit(vault_encrypted_unicode):
    # Test the rsplit method with default parameters
    result_default = vault_encrypted_unicode.rsplit()
    assert result_default == ['encrypted_value'], "The rsplit method did not return the expected list with default parameters"

    # Test the rsplit method with a specific separator
    result_with_sep = vault_encrypted_unicode.rsplit('e')
    assert result_with_sep == ['', 'ncrypt', 'd_valu', ''], "The rsplit method did not return the expected list with a specific separator"

    # Test the rsplit method with a specific separator and maxsplit
    result_with_sep_maxsplit = vault_encrypted_unicode.rsplit('e', 1)
    assert result_with_sep_maxsplit == ['encrypted_valu', ''], "The rsplit method did not return the expected list with a specific separator and maxsplit"
