# file typesystem/schemas.py:95-131
# lines [105, 106, 107, 115, 116, 117, 119, 120, 122, 125, 128, 129, 130, 131]
# branches ['100->105', '102->101', '105->106', '105->108', '106->105', '106->107', '114->115', '124->125', '127->128']

import pytest
from typesystem import Schema, fields

class MySchema(Schema):
    name = fields.String()
    age = fields.Integer(default=0)

def test_schema_initialization_coverage():
    # Test branch 102->101
    schema_instance = MySchema({"name": "Alice"})
    assert schema_instance.name == "Alice"
    
    # Test lines 105-107
    class Dummy:
        name = "Bob"
    schema_instance = MySchema(Dummy())
    assert schema_instance.name == "Bob"
    
    # Test lines 115-122
    with pytest.raises(TypeError) as exc_info:
        MySchema(name=123)  # Invalid type, should raise TypeError
    assert "Invalid argument 'name'" in str(exc_info.value)
    
    # Test line 125
    schema_instance = MySchema()
    assert schema_instance.age == 0  # Default value for age
    
    # Test lines 128-131
    with pytest.raises(TypeError) as exc_info:
        MySchema(unknown_param=123)  # Invalid keyword argument
    assert "'unknown_param' is an invalid keyword argument for MySchema()." in str(exc_info.value)
