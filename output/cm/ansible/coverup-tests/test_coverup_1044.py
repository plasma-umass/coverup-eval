# file lib/ansible/module_utils/common/collections.py:68-71
# lines [68, 71]
# branches []

import pytest
from ansible.module_utils.common.collections import is_string

# Assuming text_type and binary_type are defined in the same module or imported from another module
# If not, you would need to import them from the correct location
from ansible.module_utils.six import text_type, binary_type

class MockVaultEncryptedUnicode:
    __ENCRYPTED__ = True

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup code if necessary

def test_is_string_with_string_types(cleanup):
    assert is_string("This is a string") == True
    assert is_string(u"This is a unicode string") == True
    assert is_string(b"This is a byte string") == True

def test_is_string_with_non_string_types(cleanup):
    assert is_string(123) == False
    assert is_string([1, 2, 3]) == False
    assert is_string({'key': 'value'}) == False

def test_is_string_with_vault_encrypted_unicode(cleanup):
    vault_encrypted = MockVaultEncryptedUnicode()
    assert is_string(vault_encrypted) == True
