# file: lib/ansible/plugins/filter/core.py:264-276
# asked: {"lines": [264, 265, 266, 267, 268, 269, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [264, 265, 266, 267, 268, 269, 272, 273, 274, 275, 276], "branches": []}

import pytest
from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.plugins.filter.core import get_encrypted_password
from unittest.mock import patch

def test_get_encrypted_password_md5():
    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = 'encrypted_md5'
        result = get_encrypted_password('password', 'md5')
        assert result == 'encrypted_md5'
        mock_passlib_or_crypt.assert_called_once_with('password', 'md5_crypt', salt=None, salt_size=None, rounds=None, ident=None)

def test_get_encrypted_password_sha512():
    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = 'encrypted_sha512'
        result = get_encrypted_password('password', 'sha512')
        assert result == 'encrypted_sha512'
        mock_passlib_or_crypt.assert_called_once_with('password', 'sha512_crypt', salt=None, salt_size=None, rounds=None, ident=None)

def test_get_encrypted_password_custom_hash():
    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = 'encrypted_custom'
        result = get_encrypted_password('password', 'custom_hash')
        assert result == 'encrypted_custom'
        mock_passlib_or_crypt.assert_called_once_with('password', 'custom_hash', salt=None, salt_size=None, rounds=None, ident=None)

def test_get_encrypted_password_raises_ansible_error():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', side_effect=AnsibleError('error')) as mock_passlib_or_crypt:
        with pytest.raises(AnsibleFilterError) as excinfo:
            get_encrypted_password('password', 'sha512')
        assert 'error' in str(excinfo.value)
        mock_passlib_or_crypt.assert_called_once_with('password', 'sha512_crypt', salt=None, salt_size=None, rounds=None, ident=None)
