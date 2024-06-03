# file typesystem/tokenize/tokenize_yaml.py:112-128
# lines [127, 128]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem import Field, Schema

def test_validate_yaml(mocker):
    # Mocking the tokenize_yaml and validate_with_positions functions
    mock_tokenize_yaml = mocker.patch('typesystem.tokenize.tokenize_yaml.tokenize_yaml')
    mock_validate_with_positions = mocker.patch('typesystem.tokenize.tokenize_yaml.validate_with_positions')

    # Setting up the mock return values
    mock_tokenize_yaml.return_value = 'mocked_token'
    mock_validate_with_positions.return_value = ('mocked_value', 'mocked_error_messages')

    # Creating a dummy validator
    class DummySchema(Schema):
        pass

    # Test content
    content = "key: value"

    # Call the function
    result = validate_yaml(content, DummySchema)

    # Assertions to verify the function behavior
    mock_tokenize_yaml.assert_called_once_with(content)
    mock_validate_with_positions.assert_called_once_with(token='mocked_token', validator=DummySchema)
    assert result == ('mocked_value', 'mocked_error_messages')
