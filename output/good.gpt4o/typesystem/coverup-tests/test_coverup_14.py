# file typesystem/fields.py:81-92
# lines [81, 82, 83, 85, 87, 88, 90, 92]
# branches ['82->83', '82->85', '87->88', '87->90']

import pytest
from typesystem.fields import Field, Union

def test_field_or_operator():
    class MockField(Field):
        pass

    class MockUnion(Union):
        def __init__(self, any_of):
            self.any_of = any_of

    field1 = MockField()
    field2 = MockField()
    union1 = MockUnion([field1])
    union2 = MockUnion([field2])

    # Test Field | Field
    result = field1 | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

    # Test Union | Field
    result = union1 | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

    # Test Field | Union
    result = field1 | union2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

    # Test Union | Union
    result = union1 | union2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2, field2]

    # Clean up
    del MockField
    del MockUnion
    del field1
    del field2
    del union1
    del union2
