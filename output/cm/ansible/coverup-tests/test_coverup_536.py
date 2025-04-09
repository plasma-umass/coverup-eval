# file lib/ansible/plugins/filter/mathstuff.py:179-186
# lines [179, 181, 182, 183, 184, 185, 186]
# branches []

import pytest
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.module_utils._text import to_native
from ansible.plugins.filter.mathstuff import human_readable

# Mocking the formatters.bytes_to_human function
@pytest.fixture
def mock_formatters(mocker):
    mock = mocker.patch('ansible.plugins.filter.mathstuff.formatters.bytes_to_human')
    return mock

# Test for TypeError exception
def test_human_readable_type_error(mock_formatters):
    mock_formatters.side_effect = TypeError("Invalid input")
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_readable(size="not_a_number")
    assert "human_readable() failed on bad input:" in str(excinfo.value)

# Test for generic exception
def test_human_readable_generic_exception(mock_formatters):
    mock_formatters.side_effect = Exception("Generic error")
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_readable(size="not_a_number")
    assert "human_readable() can't interpret following string:" in str(excinfo.value)
