# file lib/ansible/parsing/yaml/objects.py:342-343
# lines [342, 343]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = "encrypted\nmultiline\ntext"
    vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)
    yield vault_obj
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_splitlines(vault_encrypted_unicode):
    # Test splitlines without keeping line endings
    lines = vault_encrypted_unicode.splitlines()
    assert lines == ["encrypted", "multiline", "text"], "Split lines without keeping ends did not match expected list"

    # Test splitlines with keeping line endings
    lines_with_ends = vault_encrypted_unicode.splitlines(keepends=True)
    assert lines_with_ends == ["encrypted\n", "multiline\n", "text"], "Split lines with keeping ends did not match expected list"
