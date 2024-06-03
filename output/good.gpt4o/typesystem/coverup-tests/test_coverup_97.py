# file typesystem/fields.py:186-189
# lines [187, 188, 189]
# branches ['187->188', '187->189']

import pytest
from typesystem.fields import String

def test_string_serialize_with_format(mocker):
    # Mock FORMATS to include a test format
    mock_formats = mocker.patch('typesystem.fields.FORMATS', {'test_format': mocker.Mock()})
    mock_formats['test_format'].serialize.return_value = 'formatted_value'
    
    # Create a String field with the test format
    field = String(format='test_format')
    
    # Serialize an object and check the result
    result = field.serialize('test_object')
    assert result == 'formatted_value'
    
    # Ensure the mock serialize method was called with the correct argument
    mock_formats['test_format'].serialize.assert_called_once_with('test_object')

def test_string_serialize_without_format():
    # Create a String field without a format
    field = String()
    
    # Serialize an object and check the result
    result = field.serialize('test_object')
    assert result == 'test_object'
