# file lib/ansible/plugins/filter/core.py:264-276
# lines [264, 265, 266, 267, 268, 269, 272, 273, 274, 275, 276]
# branches []

import pytest
from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.plugins.filter.core import get_encrypted_password
from unittest.mock import patch

def test_get_encrypted_password_sha512():
    password = "password"
    hashtype = "sha512"
    salt = "salt"
    salt_size = 16
    rounds = 5000
    ident = None

    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = "encrypted_password"
        result = get_encrypted_password(password, hashtype, salt, salt_size, rounds, ident)
        assert result == "encrypted_password"
        mock_passlib_or_crypt.assert_called_once_with(password, 'sha512_crypt', salt=salt, salt_size=salt_size, rounds=rounds, ident=ident)

def test_get_encrypted_password_md5():
    password = "password"
    hashtype = "md5"
    salt = "salt"
    salt_size = 16
    rounds = 5000
    ident = None

    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = "encrypted_password"
        result = get_encrypted_password(password, hashtype, salt, salt_size, rounds, ident)
        assert result == "encrypted_password"
        mock_passlib_or_crypt.assert_called_once_with(password, 'md5_crypt', salt=salt, salt_size=salt_size, rounds=rounds, ident=ident)

def test_get_encrypted_password_custom_hashtype():
    password = "password"
    hashtype = "custom"
    salt = "salt"
    salt_size = 16
    rounds = 5000
    ident = None

    with patch('ansible.plugins.filter.core.passlib_or_crypt') as mock_passlib_or_crypt:
        mock_passlib_or_crypt.return_value = "encrypted_password"
        result = get_encrypted_password(password, hashtype, salt, salt_size, rounds, ident)
        assert result == "encrypted_password"
        mock_passlib_or_crypt.assert_called_once_with(password, 'custom', salt=salt, salt_size=salt_size, rounds=rounds, ident=ident)

def test_get_encrypted_password_exception():
    password = "password"
    hashtype = "sha512"
    salt = "salt"
    salt_size = 16
    rounds = 5000
    ident = None

    with patch('ansible.plugins.filter.core.passlib_or_crypt', side_effect=AnsibleError("error")) as mock_passlib_or_crypt:
        with pytest.raises(AnsibleFilterError) as excinfo:
            get_encrypted_password(password, hashtype, salt, salt_size, rounds, ident)
        assert "error" in str(excinfo.value)
        mock_passlib_or_crypt.assert_called_once_with(password, 'sha512_crypt', salt=salt, salt_size=salt_size, rounds=rounds, ident=ident)
