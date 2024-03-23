# file lib/ansible/utils/hashing.py:89-92
# lines [89, 90, 91, 92]
# branches ['90->91', '90->92']

import pytest
from ansible.utils.hashing import md5s

def test_md5s_with_mocked_md5(mocker):
    # Mock the _md5 object to simulate the environment where MD5 is not available
    mocker.patch('ansible.utils.hashing._md5', None)

    # Test that md5s raises ValueError when _md5 is None
    with pytest.raises(ValueError) as exc_info:
        md5s(b"test data")

    # Assert that the exception message is as expected
    assert str(exc_info.value) == 'MD5 not available.  Possibly running in FIPS mode'
