# file typesystem/json_schema.py:565-569
# lines [565, 566, 567, 568, 569]
# branches ['567->568', '567->569']

import pytest
from typesystem.fields import Field
from typesystem.json_schema import get_standard_properties

class DefaultField(Field):
    def has_default(self):
        return True

    @property
    def default(self):
        return "default_value"

class NoDefaultField(Field):
    def has_default(self):
        return False

def test_get_standard_properties_with_default():
    field = DefaultField()
    properties = get_standard_properties(field)
    assert properties == {"default": "default_value"}

def test_get_standard_properties_without_default():
    field = NoDefaultField()
    properties = get_standard_properties(field)
    assert properties == {}
