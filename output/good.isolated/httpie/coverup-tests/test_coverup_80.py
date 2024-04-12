# file httpie/cli/requestitems.py:120-121
# lines [120, 121]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg

@pytest.fixture
def mock_key_value_arg(mocker):
    # Mocking KeyValueArg to return a specific value
    mock_arg = mocker.Mock(spec=KeyValueArg)
    mock_arg.value = "mocked_value"
    return mock_arg

def test_process_data_item_arg(mock_key_value_arg):
    from httpie.cli.requestitems import process_data_item_arg

    # Call the function with the mocked KeyValueArg
    result = process_data_item_arg(mock_key_value_arg)

    # Assert that the result is the value of the mocked KeyValueArg
    assert result == "mocked_value"
