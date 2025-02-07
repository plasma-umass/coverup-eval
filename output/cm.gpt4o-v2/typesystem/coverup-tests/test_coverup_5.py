# file: typesystem/schemas.py:9-29
# asked: {"lines": [9, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24, 25, 26, 28, 29], "branches": []}
# gained: {"lines": [9, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24, 25, 26, 28, 29], "branches": []}

import pytest
from typesystem.schemas import SchemaDefinitions

def test_schema_definitions_init():
    schema = SchemaDefinitions(a=1, b=2)
    assert schema._definitions == {'a': 1, 'b': 2}

def test_schema_definitions_getitem():
    schema = SchemaDefinitions(a=1, b=2)
    assert schema['a'] == 1
    assert schema['b'] == 2

def test_schema_definitions_iter():
    schema = SchemaDefinitions(a=1, b=2)
    keys = list(iter(schema))
    assert keys == ['a', 'b']

def test_schema_definitions_len():
    schema = SchemaDefinitions(a=1, b=2)
    assert len(schema) == 2

def test_schema_definitions_setitem():
    schema = SchemaDefinitions()
    schema['a'] = 1
    assert schema._definitions == {'a': 1}
    with pytest.raises(AssertionError):
        schema['a'] = 2

def test_schema_definitions_delitem():
    schema = SchemaDefinitions(a=1, b=2)
    del schema['a']
    assert 'a' not in schema._definitions
    assert schema._definitions == {'b': 2}
