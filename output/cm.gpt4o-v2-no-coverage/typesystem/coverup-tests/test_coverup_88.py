# file: typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest
import typing
from typesystem.schemas import Schema
from typesystem.fields import Field
from typesystem.base import ValidationError

class StringField(Field):
    def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
        if not isinstance(value, str):
            raise ValidationError("Must be a string")
        return value

class TestSchema:
    @pytest.fixture
    def schema_class(self):
        class MySchema(Schema):
            field1 = StringField()
            field2 = StringField()
        return MySchema

    def test_is_sparse_all_fields_present(self, schema_class):
        schema_instance = schema_class(field1="value1", field2="value2")
        assert not schema_instance.is_sparse

    def test_is_sparse_some_fields_missing(self, schema_class):
        schema_instance = schema_class(field1="value1")
        assert schema_instance.is_sparse

    def test_is_sparse_no_fields_present(self, schema_class):
        schema_instance = schema_class()
        assert schema_instance.is_sparse
