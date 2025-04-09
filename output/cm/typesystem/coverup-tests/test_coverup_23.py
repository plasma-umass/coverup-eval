# file typesystem/schemas.py:192-201
# lines [192, 193, 194, 195, 197, 198, 200, 201]
# branches []

import pytest
from typesystem import Schema, fields

# Assuming the SchemaMetaclass is defined elsewhere in typesystem/schemas.py
# and that it properly initializes fields and is_sparse attributes.

class ExampleSchema(Schema):
    name = fields.String()
    age = fields.Integer()

    # Adding an is_sparse property for testing purposes
    @property
    def is_sparse(self):
        return getattr(self, '_is_sparse', False)

    @is_sparse.setter
    def is_sparse(self, value):
        self._is_sparse = value

@pytest.fixture
def example_schema():
    return ExampleSchema(name="Alice", age=30)

def test_schema_repr(example_schema):
    repr_str = repr(example_schema)
    assert repr_str == "ExampleSchema(name='Alice', age=30)"
    example_schema.is_sparse = True
    repr_str_sparse = repr(example_schema)
    assert repr_str_sparse == "ExampleSchema(name='Alice', age=30) [sparse]"
