# file lib/ansible/plugins/filter/mathstuff.py:189-196
# lines [189, 191, 192, 193, 194, 195, 196]
# branches []

import pytest
from ansible.plugins.filter.mathstuff import human_to_bytes, AnsibleFilterTypeError, AnsibleFilterError

def test_human_to_bytes_valid_input(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', return_value=1024)
    assert human_to_bytes('1KB') == 1024

def test_human_to_bytes_type_error(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', side_effect=TypeError('invalid type'))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_to_bytes('invalid')
    assert "human_to_bytes() failed on bad input: invalid type" in str(excinfo.value)

def test_human_to_bytes_general_exception(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', side_effect=Exception('general error'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_to_bytes('invalid')
    assert "human_to_bytes() can't interpret following string: invalid" in str(excinfo.value)
