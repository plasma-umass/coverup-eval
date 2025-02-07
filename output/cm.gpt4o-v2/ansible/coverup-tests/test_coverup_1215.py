# file: lib/ansible/plugins/filter/mathstuff.py:189-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import human_to_bytes

def test_human_to_bytes_valid_input():
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1MB') == 1024 * 1024

def test_human_to_bytes_invalid_type(mocker):
    mocker.patch('ansible.module_utils.common.text.formatters.human_to_bytes', side_effect=TypeError('Invalid type'))
    with pytest.raises(AnsibleFilterTypeError, match="human_to_bytes\\(\\) failed on bad input: Invalid type"):
        human_to_bytes('invalid')

def test_human_to_bytes_generic_exception(mocker):
    mocker.patch('ansible.module_utils.common.text.formatters.human_to_bytes', side_effect=Exception('Generic error'))
    with pytest.raises(AnsibleFilterError, match="human_to_bytes\\(\\) can't interpret following string: invalid"):
        human_to_bytes('invalid')
