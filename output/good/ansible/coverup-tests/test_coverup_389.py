# file lib/ansible/plugins/filter/core.py:264-276
# lines [264, 265, 266, 267, 268, 269, 272, 273, 274, 275, 276]
# branches []

import pytest
from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.plugins.filter.core import get_encrypted_password
from ansible.module_utils._text import to_native
import sys

# Mocking the passlib_or_crypt function to raise an AnsibleError
def mock_passlib_or_crypt(password, hashtype, salt=None, salt_size=None, rounds=None, ident=None):
    raise AnsibleError("Mocked error")

# Test function to cover the exception branch
def test_get_encrypted_password_exception(mocker):
    mocker.patch('ansible.plugins.filter.core.passlib_or_crypt', side_effect=mock_passlib_or_crypt)
    with pytest.raises(AnsibleFilterError) as excinfo:
        get_encrypted_password("password", "sha512")
    assert "Mocked error" in to_native(excinfo.value)

# Cleanup is handled by pytest-mock through its mocker fixture, which undoes all patches after each test.
