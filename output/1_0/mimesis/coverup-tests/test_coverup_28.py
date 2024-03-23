# file mimesis/enums.py:70-78
# lines [70, 71, 73, 74, 75, 76, 77, 78]
# branches []

import pytest
from mimesis.enums import Algorithm

def test_algorithm_enum():
    # Test all members of the Algorithm enum
    assert Algorithm.MD5.value == 'md5'
    assert Algorithm.SHA1.value == 'sha1'
    assert Algorithm.SHA224.value == 'sha224'
    assert Algorithm.SHA256.value == 'sha256'
    assert Algorithm.SHA384.value == 'sha384'
    assert Algorithm.SHA512.value == 'sha512'

    # Test that all enum keys are tested
    all_keys = {'MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512'}
    enum_keys = {member.name for member in Algorithm}
    assert all_keys == enum_keys

    # Test that all enum values are tested
    all_values = {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'}
    enum_values = {member.value for member in Algorithm}
    assert all_values == enum_values
