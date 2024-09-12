# file: lib/ansible/plugins/filter/core.py:253-261
# asked: {"lines": [253, 254, 255, 256, 258, 260, 261], "branches": []}
# gained: {"lines": [253, 254, 255, 256, 258, 260, 261], "branches": []}

import pytest
import hashlib
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_bytes
from ansible.plugins.filter.core import get_hash

def test_get_hash_valid_sha1():
    data = "test"
    expected_hash = hashlib.sha1(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert get_hash(data, 'sha1') == expected_hash

def test_get_hash_valid_md5():
    data = "test"
    expected_hash = hashlib.md5(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert get_hash(data, 'md5') == expected_hash

def test_get_hash_invalid_hash_type():
    data = "test"
    with pytest.raises(AnsibleFilterError):
        get_hash(data, 'invalid_hash_type')
