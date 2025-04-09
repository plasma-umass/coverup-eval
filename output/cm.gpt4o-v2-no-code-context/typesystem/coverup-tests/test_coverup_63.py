# file: typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem import Field, Schema

def test_validate_yaml_with_string_content(monkeypatch):
    # Mocking the yaml import to ensure the assert statement is hit
    import typesystem.tokenize.tokenize_yaml as module
    monkeypatch.setattr(module, 'yaml', None)
    
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        validate_yaml("content: value", Field())

def test_validate_yaml_with_bytes_content(monkeypatch):
    # Mocking the yaml import to ensure the assert statement is hit
    import typesystem.tokenize.tokenize_yaml as module
    monkeypatch.setattr(module, 'yaml', None)
    
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        validate_yaml(b"content: value", Field())

def test_validate_yaml_with_field_validator(mocker):
    # Mocking the yaml import to ensure the assert statement is not hit
    import typesystem.tokenize.tokenize_yaml as module
    mocker.patch.object(module, 'yaml', True)
    
    # Mocking the tokenize_yaml and validate_with_positions functions
    mock_tokenize_yaml = mocker.patch('typesystem.tokenize.tokenize_yaml.tokenize_yaml', return_value='token')
    mock_validate_with_positions = mocker.patch('typesystem.tokenize.tokenize_yaml.validate_with_positions', return_value=('value', 'error_messages'))
    
    field_instance = Field()
    result = validate_yaml("content: value", field_instance)
    
    mock_tokenize_yaml.assert_called_once_with("content: value")
    mock_validate_with_positions.assert_called_once_with(token='token', validator=field_instance)
    assert result == ('value', 'error_messages')

def test_validate_yaml_with_schema_validator(mocker):
    # Mocking the yaml import to ensure the assert statement is not hit
    import typesystem.tokenize.tokenize_yaml as module
    mocker.patch.object(module, 'yaml', True)
    
    # Mocking the tokenize_yaml and validate_with_positions functions
    mock_tokenize_yaml = mocker.patch('typesystem.tokenize.tokenize_yaml.tokenize_yaml', return_value='token')
    mock_validate_with_positions = mocker.patch('typesystem.tokenize.tokenize_yaml.validate_with_positions', return_value=('value', 'error_messages'))
    
    class ExampleSchema(Schema):
        pass
    
    result = validate_yaml("content: value", ExampleSchema)
    
    mock_tokenize_yaml.assert_called_once_with("content: value")
    mock_validate_with_positions.assert_called_once_with(token='token', validator=ExampleSchema)
    assert result == ('value', 'error_messages')
