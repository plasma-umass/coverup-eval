# file: lib/ansible/parsing/yaml/objects.py:333-334
# asked: {"lines": [334], "branches": []}
# gained: {"lines": [334], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext[::-1]  # simple mock decryption (reverse the string)

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("!@#$%^&*()_+")

def test_ansible_vault_encrypted_unicode_rstrip(encrypted_unicode, mocker):
    # Mock the vault to avoid actual decryption logic
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault

    # Mock the data property to return a specific value
    mock_data = mocker.PropertyMock(return_value="!@#$%^&*()_+   ")
    type(encrypted_unicode).data = mock_data

    # Test rstrip without chars argument
    result = encrypted_unicode.rstrip()
    assert result == "!@#$%^&*()_+", f"Expected '!@#$%^&*()_+', but got {result}"

    # Test rstrip with chars argument
    result = encrypted_unicode.rstrip(" _+")
    assert result == "!@#$%^&*()", f"Expected '!@#$%^&*()', but got {result}"
