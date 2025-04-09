# file: lib/ansible/parsing/yaml/objects.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, vault, ciphertext):
        self.vault = vault
        self._ciphertext = ciphertext

@pytest.fixture
def mock_vault(mocker):
    mock_vault = mocker.Mock()
    mock_vault.decrypt.return_value = "decrypted_data"
    return mock_vault

@pytest.fixture
def mock_ciphertext():
    return "mock_encrypted_data"

def test_ansible_vault_encrypted_unicode_str(mock_vault, mock_ciphertext):
    obj = MockAnsibleVaultEncryptedUnicode(mock_vault, mock_ciphertext)
    result = str(obj)
    assert result == to_native("decrypted_data", errors='surrogate_or_strict')

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
