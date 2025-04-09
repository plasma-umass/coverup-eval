# file lib/ansible/parsing/yaml/objects.py:140-141
# lines [141]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, '__init__', return_value=None)
    av = AnsibleVaultEncryptedUnicode()
    av.vault = mocker.MagicMock()
    av._ciphertext = 'encrypted_data'
    av.vault.decrypt.return_value = 'decrypted_data'
    return av

def test_ansible_vault_encrypted_unicode_encode(mock_ansible_vault_encrypted_unicode):
    # Setup
    av = mock_ansible_vault_encrypted_unicode
    encoding = 'utf-8'
    errors = 'strict'

    # Exercise
    result = av.encode(encoding=encoding, errors=errors)

    # Verify
    assert result == to_bytes(av.vault.decrypt.return_value, encoding=encoding, errors=errors)
    assert isinstance(result, bytes)

    # Cleanup - nothing to do since we used a fixture with mocker
