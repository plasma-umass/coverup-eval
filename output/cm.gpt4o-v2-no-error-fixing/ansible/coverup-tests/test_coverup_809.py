# file: lib/ansible/module_utils/common/validation.py:554-564
# asked: {"lines": [561, 562, 563, 564], "branches": []}
# gained: {"lines": [561, 562, 563, 564], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_bits

def test_check_type_bits_valid():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('2Kb') == 2048

def test_check_type_bits_invalid():
    with pytest.raises(TypeError, match=".* cannot be converted to a Bit value"):
        check_type_bits('1MB')
    with pytest.raises(TypeError, match=".* cannot be converted to a Bit value"):
        check_type_bits('invalid')

def test_check_type_bits_empty_string():
    with pytest.raises(TypeError, match=".* cannot be converted to a Bit value"):
        check_type_bits('')

def test_check_type_bits_no_unit():
    assert check_type_bits('1024') == 1024
