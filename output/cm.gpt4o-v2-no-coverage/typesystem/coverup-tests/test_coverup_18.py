# file: typesystem/fields.py:81-92
# asked: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}
# gained: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}

import pytest
from typesystem.fields import Field, Union

class MockField(Field):
    def __init__(self, name, allow_null=False):
        self.name = name
        self.allow_null = allow_null

def test_field_or_with_non_union():
    field1 = MockField("field1")
    field2 = MockField("field2")
    result = field1 | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_field_or_with_union():
    field1 = MockField("field1")
    field2 = MockField("field2")
    union_field = Union(any_of=[field1])
    result = union_field | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_field_or_with_both_unions():
    field1 = MockField("field1")
    field2 = MockField("field2")
    field3 = MockField("field3")
    union_field1 = Union(any_of=[field1])
    union_field2 = Union(any_of=[field2])
    result = union_field1 | union_field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Cleanup code if necessary
    yield
    # Reset any state if necessary
