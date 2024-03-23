# file lib/ansible/modules/rpm_key.py:92-95
# lines [92, 94, 95]
# branches []

import pytest
import re
from ansible.module_utils._text import to_native

# Assuming the is_pubkey function is part of a module named rpm_key
# and that the module is located at lib/ansible/modules/rpm_key.py
# Adjust the import path according to the actual structure of the ansible project.
from ansible.modules.rpm_key import is_pubkey

@pytest.fixture(scope="function")
def pubkey_sample():
    return """
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1.4.5 (GNU/Linux)
    
    mQGiBEr3xR8RBAC1c8ZVC3/b5xGZp8x4ppxy+G8F3+IjukXY/hy2k5iBd1sI
    ...
    hP9HO9f/s/EzVQ==
    =iwOZ
    -----END PGP PUBLIC KEY BLOCK-----
    """

@pytest.fixture(scope="function")
def not_pubkey_sample():
    return """
    This is not a PGP public key block.
    It does not contain the correct BEGIN and END markers.
    """

def test_is_pubkey_with_valid_key(pubkey_sample):
    assert is_pubkey(pubkey_sample), "The function should return True for a valid PGP public key block."

def test_is_pubkey_with_invalid_key(not_pubkey_sample):
    assert not is_pubkey(not_pubkey_sample), "The function should return False for an invalid PGP public key block."
