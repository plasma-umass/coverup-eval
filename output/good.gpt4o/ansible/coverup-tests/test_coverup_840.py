# file lib/ansible/plugins/filter/core.py:71-73
# lines [71, 73]
# branches []

import pytest
from ansible.plugins.filter.core import to_nice_json

def test_to_nice_json(mocker):
    # Mock the to_json function to ensure it is called with the correct parameters
    mock_to_json = mocker.patch('ansible.plugins.filter.core.to_json', return_value='mocked_json')

    # Test data
    data = {'key': 'value'}

    # Call the function
    result = to_nice_json(data)

    # Verify the result
    assert result == 'mocked_json'

    # Verify that to_json was called with the correct parameters
    mock_to_json.assert_called_once_with(data, indent=4, sort_keys=True, separators=(',', ': '))

    # Clean up the mock
    mock_to_json.stop()
