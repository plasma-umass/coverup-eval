# file typesystem/schemas.py:166-173
# lines [167, 168, 170, 171, 172, 173]
# branches ['167->168', '167->170', '170->171', '170->173', '171->170', '171->172']

import pytest
from typesystem import Schema, fields

# Assuming the Schema class is defined as provided in the snippet
# and has a fields attribute that is a dictionary of its fields.

class MySchema(Schema):
    field1 = fields.Integer()
    field2 = fields.String()

def test_schema_equality():
    schema1 = MySchema(field1=1, field2='a')
    schema2 = MySchema(field1=1, field2='a')
    schema3 = MySchema(field1=2, field2='b')
    schema4 = 'not_a_schema'

    # Test equality with the same class and same values
    assert schema1 == schema2

    # Test equality with the same class but different values
    assert not (schema1 == schema3)

    # Test equality with a different class
    assert not (schema1 == schema4)
