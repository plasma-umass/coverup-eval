# file lib/ansible/parsing/yaml/objects.py:256-257
# lines [257]
# branches []

import sys
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield vault_str
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_index(vault_encrypted_unicode):
    # Test the index method for a substring that exists
    sub_str = 'crypt'
    start = 1
    end = sys.maxsize
    assert vault_encrypted_unicode.index(sub_str, start, end) == vault_encrypted_unicode.data.index(sub_str, start, end)

    # Test the index method for a substring that does not exist and should raise a ValueError
    with pytest.raises(ValueError):
        vault_encrypted_unicode.index('nonexistent', start, end)
