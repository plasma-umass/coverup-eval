# file lib/ansible/parsing/yaml/objects.py:106-110
# lines [106, 107, 108, 109, 110]
# branches ['108->109', '108->110']

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    @pytest.fixture
    def mock_vault(self):
        return Mock()

    @pytest.fixture
    def encrypted_unicode(self, mock_vault):
        obj = AnsibleVaultEncryptedUnicode(b'some_encrypted_text')
        obj.vault = mock_vault
        return obj

    def test_data_without_vault(self, encrypted_unicode):
        encrypted_unicode.vault = None
        result = encrypted_unicode.data
        assert result == 'some_encrypted_text'

    def test_data_with_vault(self, encrypted_unicode, mock_vault):
        mock_vault.decrypt.return_value = b'decrypted_text'
        result = encrypted_unicode.data
        mock_vault.decrypt.assert_called_once_with(b'some_encrypted_text', obj=encrypted_unicode)
        assert result == 'decrypted_text'
