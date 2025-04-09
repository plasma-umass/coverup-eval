# file lib/ansible/plugins/filter/core.py:253-261
# lines [253, 254, 255, 256, 258, 260, 261]
# branches []

import hashlib
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import get_hash
from ansible.module_utils._text import to_bytes

def test_get_hash_valid_hash_type():
    data = "test_data"
    hashtype = "sha256"
    expected_hash = hashlib.new(hashtype)
    expected_hash.update(to_bytes(data, errors='surrogate_or_strict'))
    
    result = get_hash(data, hashtype)
    assert result == expected_hash.hexdigest()

def test_get_hash_invalid_hash_type(mocker):
    data = "test_data"
    hashtype = "invalid_hash"
    mocker.patch('hashlib.new', side_effect=ValueError("unsupported hash type"))
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        get_hash(data, hashtype)
    assert "unsupported hash type" in str(excinfo.value)
