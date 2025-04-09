# file typesystem/tokenize/tokenize_yaml.py:112-128
# lines [127, 128]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem.fields import Field
from typesystem.schemas import Schema

@pytest.fixture
def mock_tokenize_yaml(mocker):
    return mocker.patch('typesystem.tokenize.tokenize_yaml.tokenize_yaml')

@pytest.fixture
def mock_validate_with_positions(mocker):
    return mocker.patch('typesystem.tokenize.tokenize_yaml.validate_with_positions')

def test_validate_yaml_executes_missing_lines(mock_tokenize_yaml, mock_validate_with_positions):
    class DummySchema(Schema):
        pass

    content = "key: value"
    validator = DummySchema

    mock_tokenize_yaml.return_value = 'mocked_token'
    mock_validate_with_positions.return_value = ('mocked_value', 'mocked_error_messages')

    value, error_messages = validate_yaml(content, validator)

    mock_tokenize_yaml.assert_called_once_with(content)
    mock_validate_with_positions.assert_called_once_with(token='mocked_token', validator=validator)
    assert value == 'mocked_value'
    assert error_messages == 'mocked_error_messages'
