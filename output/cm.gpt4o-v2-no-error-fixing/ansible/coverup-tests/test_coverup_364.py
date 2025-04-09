# file: lib/ansible/plugins/filter/mathstuff.py:189-196
# asked: {"lines": [189, 191, 192, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [189, 191, 192, 193, 194, 195, 196], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import human_to_bytes

def test_human_to_bytes_valid_input():
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1TB') == 1099511627776

def test_human_to_bytes_invalid_type_error(mocker):
    mocker.patch('ansible.module_utils.common.text.formatters.human_to_bytes', side_effect=TypeError('Invalid type'))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_to_bytes('invalid')
    assert 'human_to_bytes() failed on bad input' in str(excinfo.value)

def test_human_to_bytes_generic_error(mocker):
    mocker.patch('ansible.module_utils.common.text.formatters.human_to_bytes', side_effect=Exception('Generic error'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_to_bytes('invalid')
    assert "human_to_bytes() can't interpret following string" in str(excinfo.value)
