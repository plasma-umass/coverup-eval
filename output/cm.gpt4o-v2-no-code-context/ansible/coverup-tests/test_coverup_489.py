# file: lib/ansible/plugins/filter/core.py:253-261
# asked: {"lines": [253, 254, 255, 256, 258, 260, 261], "branches": []}
# gained: {"lines": [253, 254, 255, 256, 258, 260, 261], "branches": []}

import pytest
import hashlib
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import get_hash

def test_get_hash_valid_sha1():
    result = get_hash('test data', 'sha1')
    expected = hashlib.sha1(b'test data').hexdigest()
    assert result == expected

def test_get_hash_valid_md5():
    result = get_hash('test data', 'md5')
    expected = hashlib.md5(b'test data').hexdigest()
    assert result == expected

def test_get_hash_invalid_hash_type():
    with pytest.raises(AnsibleFilterError):
        get_hash('test data', 'invalid_hash')

def test_get_hash_non_string_data():
    result = get_hash(12345, 'sha1')
    expected = hashlib.sha1(b'12345').hexdigest()
    assert result == expected
