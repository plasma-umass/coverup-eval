# file: lib/ansible/module_utils/common/validation.py:543-551
# asked: {"lines": [548, 549, 550, 551], "branches": []}
# gained: {"lines": [548, 549, 550, 551], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_bytes

def test_check_type_bytes_valid():
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1G') == 1073741824

def test_check_type_bytes_invalid():
    with pytest.raises(TypeError, match=".* cannot be converted to a Byte value"):
        check_type_bytes('invalid')

    with pytest.raises(TypeError, match=".* cannot be converted to a Byte value"):
        check_type_bytes('1Mb')

    with pytest.raises(TypeError, match=".* cannot be converted to a Byte value"):
        check_type_bytes('1XB')
