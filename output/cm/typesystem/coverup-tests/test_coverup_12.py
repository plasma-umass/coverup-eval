# file typesystem/schemas.py:9-29
# lines [9, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24, 25, 26, 28, 29]
# branches []

import pytest
from typesystem.schemas import SchemaDefinitions

def test_schema_definitions():
    schema_definitions = SchemaDefinitions()

    # Test __setitem__ and __getitem__
    schema_definitions['a'] = 1
    assert schema_definitions['a'] == 1

    # Test __iter__ and __len__
    assert len(schema_definitions) == 1
    assert list(iter(schema_definitions)) == ['a']

    # Test __delitem__
    del schema_definitions['a']
    assert len(schema_definitions) == 0

    # Test __setitem__ with an existing key
    schema_definitions['a'] = 1
    with pytest.raises(AssertionError) as excinfo:
        schema_definitions['a'] = 2
    assert "Definition for 'a' has already been set." in str(excinfo.value).format(key='a')
