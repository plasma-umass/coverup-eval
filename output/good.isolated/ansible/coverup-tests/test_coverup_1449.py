# file lib/ansible/parsing/yaml/objects.py:330-331
# lines [331]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(mocker):
    # Mock the AnsibleVaultEncryptedUnicode object with a specific data value
    mocker.patch.object(AnsibleVaultEncryptedUnicode, '__init__', return_value=None)
    av = AnsibleVaultEncryptedUnicode()
    av.vault = mocker.MagicMock()
    av._ciphertext = "encrypted_value"
    mocker.patch.object(av.vault, 'decrypt', return_value=av._ciphertext)
    return av

def test_ansible_vault_encrypted_unicode_rpartition(mock_ansible_vault_encrypted_unicode):
    # Test the rpartition method
    av = mock_ansible_vault_encrypted_unicode
    left, sep, right = av.rpartition("_")
    assert left == "encrypted"
    assert sep == "_"
    assert right == "value"
