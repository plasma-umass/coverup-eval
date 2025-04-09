# file: typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest
from typesystem.schemas import Schema

class TestSchema:
    def test_is_sparse_true(self, monkeypatch):
        class TestSchema(Schema):
            fields = {'field1': int, 'field2': str}

        schema_instance = TestSchema()
        
        # Ensure that the schema instance does not have the 'field1' and 'field2' attributes
        monkeypatch.setattr(schema_instance, 'fields', {'field1': int, 'field2': str})
        
        assert schema_instance.is_sparse is True

    def test_is_sparse_false(self, monkeypatch):
        class TestSchema(Schema):
            fields = {'field1': int, 'field2': str}

            def __init__(self):
                self.field1 = 1
                self.field2 = 'value'

        schema_instance = TestSchema()
        
        assert schema_instance.is_sparse is False
