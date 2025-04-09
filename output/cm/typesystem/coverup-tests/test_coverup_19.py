# file typesystem/schemas.py:184-187
# lines [184, 185, 186, 187]
# branches ['185->exit', '185->186', '186->185', '186->187']

import pytest
from typesystem import Schema

# Assuming the SchemaMetaclass is defined elsewhere in typesystem.schemas
# and that it properly initializes `fields` attribute in the Schema class.

class ExampleSchema(Schema):
    pass

@pytest.fixture
def example_schema():
    schema = ExampleSchema()
    schema.fields = ['field1', 'field2']
    setattr(schema, 'field1', 'value1')
    # intentionally not setting schema.field2 to test the hasattr check
    return schema

def test_schema_iter(example_schema):
    # Test __iter__ method to ensure it only yields fields that have been set
    iterated_fields = list(iter(example_schema))
    assert 'field1' in iterated_fields
    assert 'field2' not in iterated_fields  # because field2 is not set

    # Clean up after test
    delattr(example_schema, 'field1')
