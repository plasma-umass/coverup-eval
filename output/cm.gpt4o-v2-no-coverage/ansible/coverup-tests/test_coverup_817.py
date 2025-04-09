# file: lib/ansible/modules/rpm_key.py:92-95
# asked: {"lines": [92, 94, 95], "branches": []}
# gained: {"lines": [92, 94, 95], "branches": []}

import pytest
from ansible.module_utils._text import to_native
from ansible.modules.rpm_key import is_pubkey

def test_is_pubkey_valid_key():
    valid_key = """
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1

    mQENBFMiiGkBCAC5+f...
    -----END PGP PUBLIC KEY BLOCK-----
    """
    assert is_pubkey(valid_key) == True

def test_is_pubkey_invalid_key():
    invalid_key = "This is not a valid PGP key"
    assert is_pubkey(invalid_key) == False

def test_is_pubkey_partial_key():
    partial_key = """
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1

    mQENBFMiiGkBCAC5+f...
    """
    assert is_pubkey(partial_key) == False

def test_is_pubkey_empty_string():
    empty_string = ""
    assert is_pubkey(empty_string) == False
