# file: lib/ansible/utils/hashing.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}
# gained: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}

import pytest
from hashlib import md5 as _md5
from ansible.utils.hashing import md5, secure_hash
from ansible.errors import AnsibleError

def test_md5(monkeypatch, tmp_path):
    # Create a temporary file
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("This is a test file.")

    # Test when _md5 is available
    assert md5(str(test_file)) == secure_hash(str(test_file), _md5)

    # Test when _md5 is not available
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5(str(test_file))
