# file lib/ansible/module_utils/common/validation.py:554-564
# lines [554, 561, 562, 563, 564]
# branches []

import pytest
from ansible.module_utils.common.validation import check_type_bits

def test_check_type_bits_valid(mocker):
    mocker.patch('ansible.module_utils.common.validation.human_to_bytes', return_value=1048576)
    assert check_type_bits('1Mb') == 1048576

def test_check_type_bits_invalid(mocker):
    mocker.patch('ansible.module_utils.common.validation.human_to_bytes', side_effect=ValueError)
    with pytest.raises(TypeError) as excinfo:
        check_type_bits('invalid')
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a Bit value"
