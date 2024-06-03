# file typesystem/fields.py:106-141
# lines [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141]
# branches ['124->125', '124->127', '133->134', '133->136', '136->137', '136->140']

import pytest
import re
from typesystem.fields import Field

class TestStringField:
    def test_string_field_initialization(self):
        from typesystem.fields import String

        # Test with all default parameters
        field = String()
        assert field.allow_blank == False
        assert field.trim_whitespace == True
        assert field.max_length is None
        assert field.min_length is None
        assert field.pattern is None
        assert field.pattern_regex is None
        assert field.format is None

        # Test with custom parameters
        field = String(
            allow_blank=True,
            trim_whitespace=False,
            max_length=10,
            min_length=5,
            pattern=r'^[a-z]+$',
            format='email'
        )
        assert field.allow_blank == True
        assert field.trim_whitespace == False
        assert field.max_length == 10
        assert field.min_length == 5
        assert field.pattern == r'^[a-z]+$'
        assert field.pattern_regex.pattern == r'^[a-z]+$'
        assert field.format == 'email'

        # Test with pattern as a compiled regex
        pattern = re.compile(r'^[0-9]+$')
        field = String(pattern=pattern)
        assert field.pattern == r'^[0-9]+$'
        assert field.pattern_regex == pattern

        # Test with allow_blank and no default
        field = String(allow_blank=True)
        assert field.default == ""

    def test_string_field_invalid_initialization(self):
        from typesystem.fields import String

        with pytest.raises(AssertionError):
            String(max_length='not-an-int')

        with pytest.raises(AssertionError):
            String(min_length='not-an-int')

        with pytest.raises(AssertionError):
            String(pattern=123)

        with pytest.raises(AssertionError):
            String(format=123)
