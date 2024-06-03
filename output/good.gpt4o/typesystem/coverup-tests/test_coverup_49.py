# file typesystem/fields.py:736-742
# lines [736, 737, 741, 742]
# branches []

import pytest
import typing
from typesystem.fields import Field

class TestAnyField:
    def test_any_field_validate(self):
        class Any(Field):
            """
            Always matches.
            """
        
            def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
                return value

        any_field = Any()
        
        # Test with various types of values
        assert any_field.validate(123) == 123
        assert any_field.validate("test") == "test"
        assert any_field.validate([1, 2, 3]) == [1, 2, 3]
        assert any_field.validate({"key": "value"}) == {"key": "value"}
        assert any_field.validate(None) == None
        assert any_field.validate(123.456) == 123.456
        assert any_field.validate(True) == True
        assert any_field.validate(False) == False
