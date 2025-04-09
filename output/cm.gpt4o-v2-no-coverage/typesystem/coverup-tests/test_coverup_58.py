# file: typesystem/schemas.py:95-131
# asked: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 103], [105, 106], [105, 108], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 125], [127, 0], [127, 128]]}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import String, Integer
from typesystem.base import ValidationResult, ValidationError, Message

class TestSchema(Schema):
    name = String()
    age = Integer()

def test_schema_init_with_dict():
    data = {"name": "John", "age": 30}
    schema = TestSchema(data)
    assert schema.name == "John"
    assert schema.age == 30

def test_schema_init_with_object():
    class Data:
        name = "John"
        age = 30

    data = Data()
    schema = TestSchema(data)
    assert schema.name == "John"
    assert schema.age == 30

def test_schema_init_with_kwargs():
    schema = TestSchema(name="John", age=30)
    assert schema.name == "John"
    assert schema.age == 30

def test_schema_init_with_invalid_kwargs():
    with pytest.raises(TypeError) as excinfo:
        TestSchema(name="John", age=30, invalid="value")
    assert "invalid' is an invalid keyword argument for TestSchema()." in str(excinfo.value)

def test_schema_init_with_validation_error(mocker):
    mock_field = mocker.patch.object(TestSchema.fields['age'], 'validate_or_error', return_value=(None, ValidationError(messages=[Message(text="Invalid age")])))
    with pytest.raises(TypeError) as excinfo:
        TestSchema(name="John", age="invalid")
    assert "Invalid argument 'age' for TestSchema(). Invalid age" in str(excinfo.value)
    mock_field.assert_called_once_with("invalid")

def test_schema_init_with_default_value(mocker):
    mock_field = mocker.patch.object(TestSchema.fields['age'], 'has_default', return_value=True)
    mock_default = mocker.patch.object(TestSchema.fields['age'], 'get_default_value', return_value=25)
    schema = TestSchema(name="John")
    assert schema.name == "John"
    assert schema.age == 25
    mock_field.assert_called_once()
    mock_default.assert_called_once()
