# file: typesystem/schemas.py:95-131
# asked: {"lines": [97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 128, 129, 130, 131], "branches": [[96, 97], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 128]]}
# gained: {"lines": [97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 128, 129, 130, 131], "branches": [[96, 97], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 128]]}

import pytest
from typesystem.schemas import Schema

class MockSchema:
    def __init__(self, has_default=False, default_value=None):
        self._has_default = has_default
        self._default_value = default_value

    def validate_or_error(self, value):
        if value == "invalid":
            return value, MockError()
        return value, None

    def has_default(self):
        return self._has_default

    def get_default_value(self):
        return self._default_value

class MockError:
    def messages(self):
        return [MockMessage("error message")]

class MockMessage:
    def __init__(self, text):
        self.text = text

@pytest.fixture
def mock_schema(monkeypatch):
    fields = {
        "field1": MockSchema(),
        "field2": MockSchema(has_default=True, default_value="default"),
    }
    monkeypatch.setattr(Schema, "fields", fields)
    return Schema

def test_schema_init_with_args_dict(mock_schema):
    schema = mock_schema({"field1": "value1"})
    assert schema.field1 == "value1"
    assert not hasattr(schema, "field2")

def test_schema_init_with_args_object(mock_schema):
    class MockObject:
        field1 = "value1"

    schema = mock_schema(MockObject())
    assert schema.field1 == "value1"
    assert not hasattr(schema, "field2")

def test_schema_init_with_kwargs_valid(mock_schema):
    schema = mock_schema(field1="value1")
    assert schema.field1 == "value1"
    assert schema.field2 == "default"

def test_schema_init_with_kwargs_invalid(mock_schema):
    with pytest.raises(TypeError) as excinfo:
        mock_schema(field1="invalid")
    assert "Invalid argument 'field1'" in str(excinfo.value)

def test_schema_init_with_extra_kwargs(mock_schema):
    with pytest.raises(TypeError) as excinfo:
        mock_schema(field3="value3")
    assert "'field3' is an invalid keyword argument" in str(excinfo.value)
