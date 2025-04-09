# file lib/ansible/plugins/filter/core.py:253-261
# lines [253, 254, 255, 256, 258, 260, 261]
# branches []

import pytest
import hashlib
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_bytes
from ansible.plugins.filter.core import get_hash

def test_get_hash_valid_sha1():
    data = "test data"
    expected_hash = hashlib.sha1(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert get_hash(data) == expected_hash

def test_get_hash_invalid_hashtype():
    data = "test data"
    with pytest.raises(AnsibleFilterError):
        get_hash(data, hashtype='invalid_hash')

def test_get_hash_valid_md5():
    data = "test data"
    expected_hash = hashlib.md5(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert get_hash(data, hashtype='md5') == expected_hash
