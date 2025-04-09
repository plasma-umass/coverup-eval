# file lib/ansible/module_utils/common/validation.py:543-551
# lines [543, 548, 549, 550, 551]
# branches []

import pytest
from ansible.module_utils.common.validation import check_type_bytes

def test_check_type_bytes_valid(mocker):
    mock_human_to_bytes = mocker.patch('ansible.module_utils.common.validation.human_to_bytes')
    mock_human_to_bytes.return_value = 1024
    assert check_type_bytes('1k') == 1024

def test_check_type_bytes_invalid(mocker):
    mock_human_to_bytes = mocker.patch('ansible.module_utils.common.validation.human_to_bytes')
    mock_human_to_bytes.side_effect = ValueError
    with pytest.raises(TypeError) as excinfo:
        check_type_bytes('invalid')
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a Byte value"
