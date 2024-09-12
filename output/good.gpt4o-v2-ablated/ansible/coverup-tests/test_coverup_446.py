# file: lib/ansible/plugins/filter/mathstuff.py:189-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": []}

import pytest
from ansible.plugins.filter.mathstuff import human_to_bytes, AnsibleFilterTypeError, AnsibleFilterError
from ansible.module_utils._text import to_native
from unittest.mock import patch

def test_human_to_bytes_valid_input():
    with patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', return_value=1024) as mock_formatter:
        result = human_to_bytes('1KB')
        assert result == 1024
        mock_formatter.assert_called_once_with('1KB', None, False)

def test_human_to_bytes_invalid_type():
    with patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', side_effect=TypeError('Invalid type')):
        with pytest.raises(AnsibleFilterTypeError) as excinfo:
            human_to_bytes(123)
        assert "human_to_bytes() failed on bad input: Invalid type" in str(excinfo.value)

def test_human_to_bytes_generic_exception():
    with patch('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', side_effect=Exception('Generic error')):
        with pytest.raises(AnsibleFilterError) as excinfo:
            human_to_bytes('invalid')
        assert "human_to_bytes() can't interpret following string: invalid" in str(excinfo.value)
