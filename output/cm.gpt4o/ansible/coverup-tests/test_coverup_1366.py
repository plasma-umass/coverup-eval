# file lib/ansible/parsing/yaml/objects.py:116-117
# lines [117]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    @pytest.fixture
    def mock_vault(self):
        return Mock()

    @pytest.fixture
    def encrypted_unicode(self, mock_vault):
        obj = AnsibleVaultEncryptedUnicode(ciphertext=b"dummy_ciphertext")
        obj.vault = mock_vault
        return obj

    def test_is_encrypted(self, encrypted_unicode, mock_vault):
        # Mock the is_encrypted method to return True
        mock_vault.is_encrypted.return_value = True
        
        # Call the method
        result = encrypted_unicode.is_encrypted()
        
        # Assert the method was called with the correct argument
        mock_vault.is_encrypted.assert_called_once_with(b"dummy_ciphertext")
        
        # Assert the result is True
        assert result is True
