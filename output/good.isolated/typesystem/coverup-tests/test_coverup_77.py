# file typesystem/schemas.py:142-148
# lines [142, 143, 144, 146, 147, 148]
# branches []

import pytest
from typesystem import ValidationError
from typesystem.fields import Field
from typesystem.schemas import Schema

# Assuming the Schema class is part of a larger module that we're testing

class ExampleSchema(Schema):
    example_field = Field()

def test_schema_validate_success(mocker):
    # Mock the make_validator and validate methods
    mock_validator = mocker.Mock()
    mock_validator.validate.return_value = {'example_field': 'value'}
    mocker.patch.object(ExampleSchema, 'make_validator', return_value=mock_validator)

    # Test the validate class method with correct data
    result = ExampleSchema.validate({'example_field': 'value'})
    assert isinstance(result, ExampleSchema)
    assert result['example_field'] == 'value'
    ExampleSchema.make_validator.assert_called_once_with(strict=False)
    mock_validator.validate.assert_called_once_with({'example_field': 'value'}, strict=False)

def test_schema_validate_strict_success(mocker):
    # Mock the make_validator and validate methods
    mock_validator = mocker.Mock()
    mock_validator.validate.return_value = {'example_field': 'value'}
    mocker.patch.object(ExampleSchema, 'make_validator', return_value=mock_validator)

    # Test the validate class method with strict=True
    result = ExampleSchema.validate({'example_field': 'value'}, strict=True)
    assert isinstance(result, ExampleSchema)
    assert result['example_field'] == 'value'
    ExampleSchema.make_validator.assert_called_once_with(strict=True)
    mock_validator.validate.assert_called_once_with({'example_field': 'value'}, strict=True)

def test_schema_validate_failure(mocker):
    # Mock the make_validator and validate methods to raise ValidationError
    mock_validator = mocker.Mock()
    validation_error = ValidationError(text="Invalid data")
    mock_validator.validate.side_effect = validation_error
    mocker.patch.object(ExampleSchema, 'make_validator', return_value=mock_validator)

    # Test the validate class method with incorrect data
    with pytest.raises(ValidationError) as exc_info:
        ExampleSchema.validate({'example_field': 'invalid'})
    assert str(exc_info.value) == "Invalid data"
    ExampleSchema.make_validator.assert_called_once_with(strict=False)
    mock_validator.validate.assert_called_once_with({'example_field': 'invalid'}, strict=False)
