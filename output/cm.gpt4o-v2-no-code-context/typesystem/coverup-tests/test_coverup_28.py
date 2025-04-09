# file: typesystem/schemas.py:184-187
# asked: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 187]]}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass

class TestSchema:
    def test_schema_iter(self):
        class TestSchema(Schema):
            fields = {'field1': str, 'field2': int}

            def __init__(self):
                self.field1 = 'value1'
                self.field2 = 42

        schema_instance = TestSchema()
        schema_instance.fields = {'field1': str, 'field2': int}
        keys = list(schema_instance.__iter__())
        
        assert 'field1' in keys
        assert 'field2' in keys
        assert len(keys) == 2
