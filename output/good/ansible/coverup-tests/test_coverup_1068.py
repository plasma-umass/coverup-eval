# file lib/ansible/parsing/yaml/objects.py:242-243
# lines [242, 243]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_expandtabs(vault_encrypted_unicode):
    # Given a string with tabs
    vault_encrypted_unicode.data = "a\tb\tc"

    # When expandtabs is called with a specific tabsize
    result = vault_encrypted_unicode.expandtabs(tabsize=4)

    # Then the tabs should be expanded accordingly
    assert result == "a   b   c", "The expandtabs method did not expand tabs correctly"

    # When expandtabs is called without specifying tabsize
    result = vault_encrypted_unicode.expandtabs()

    # Then the tabs should be expanded using the default tabsize of 8
    assert result == "a       b       c", "The expandtabs method did not use the default tabsize correctly"
