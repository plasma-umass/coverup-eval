# file lib/ansible/plugins/filter/mathstuff.py:189-196
# lines [189, 191, 192, 193, 194, 195, 196]
# branches []

import pytest
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.plugins.filter.mathstuff import human_to_bytes
from ansible.module_utils._text import to_native

# Mocking the formatters module and its human_to_bytes function
@pytest.fixture
def mock_formatters(mocker):
    mock = mocker.patch('ansible.plugins.filter.mathstuff.formatters')
    return mock

# Test to cover the TypeError exception branch
def test_human_to_bytes_type_error(mock_formatters):
    mock_formatters.human_to_bytes.side_effect = TypeError("Invalid input")
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_to_bytes("invalid", default_unit="MiB")
    assert "human_to_bytes() failed on bad input:" in str(excinfo.value)

# Test to cover the generic Exception branch
def test_human_to_bytes_generic_exception(mock_formatters):
    mock_formatters.human_to_bytes.side_effect = Exception("Uninterpretable string")
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_to_bytes("uninterpretable")
    assert "human_to_bytes() can't interpret following string:" in str(excinfo.value)
