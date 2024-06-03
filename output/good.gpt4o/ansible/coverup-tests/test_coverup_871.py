# file lib/ansible/plugins/filter/core.py:460-461
# lines [460, 461]
# branches []

import pytest
from ansible.plugins.filter.core import b64encode

def test_b64encode(mocker):
    # Mocking to_text and to_bytes to ensure they are called correctly
    mock_to_text = mocker.patch('ansible.plugins.filter.core.to_text', wraps=lambda x: x.decode('utf-8'))
    mock_to_bytes = mocker.patch('ansible.plugins.filter.core.to_bytes', wraps=lambda x, encoding, errors: x.encode(encoding, errors=errors))

    # Test data
    test_string = "test"
    expected_encoded_string = "dGVzdA=="

    # Call the function
    result = b64encode(test_string)

    # Assertions
    assert result == expected_encoded_string
    mock_to_bytes.assert_called_once_with(test_string, encoding='utf-8', errors='surrogate_or_strict')
    mock_to_text.assert_called_once()
