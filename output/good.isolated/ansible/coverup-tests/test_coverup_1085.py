# file lib/ansible/parsing/yaml/objects.py:324-325
# lines [324, 325]
# branches []

import sys
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_rindex(vault_encrypted_unicode):
    # Prepare the data
    vault_encrypted_unicode.data = "some_encrypted_data_here"
    sub_string = "encrypted"
    start = 0
    end = sys.maxsize

    # Call the method
    index = vault_encrypted_unicode.rindex(sub_string, start, end)

    # Assert the postconditions
    assert index == vault_encrypted_unicode.data.rindex(sub_string, start, end)
