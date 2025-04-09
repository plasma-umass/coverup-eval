# file: lib/ansible/plugins/filter/core.py:264-276
# asked: {"lines": [265, 266, 267, 268, 269, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [265, 266, 267, 268, 269, 272, 273, 274, 275, 276], "branches": []}

import pytest
from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.plugins.filter.core import get_encrypted_password
from ansible.utils.encrypt import passlib_or_crypt

def test_get_encrypted_password_md5():
    result = get_encrypted_password('password', 'md5')
    assert result is not None

def test_get_encrypted_password_blowfish():
    result = get_encrypted_password('password', 'blowfish')
    assert result is not None

def test_get_encrypted_password_sha256():
    result = get_encrypted_password('password', 'sha256')
    assert result is not None

def test_get_encrypted_password_sha512():
    result = get_encrypted_password('password', 'sha512')
    assert result is not None

def test_get_encrypted_password_invalid_hashtype(monkeypatch):
    def mock_passlib_or_crypt(secret, algorithm, salt=None, salt_size=None, rounds=None, ident=None):
        raise AnsibleError('Mocked error')
    
    monkeypatch.setattr('ansible.utils.encrypt.passlib_or_crypt', mock_passlib_or_crypt)
    
    with pytest.raises(AnsibleFilterError):
        get_encrypted_password('password', 'invalid_hashtype')
