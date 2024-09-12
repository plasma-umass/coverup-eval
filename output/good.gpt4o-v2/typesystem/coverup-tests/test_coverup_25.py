# file: typesystem/json_schema.py:565-569
# asked: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}
# gained: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}

import pytest
from typesystem.fields import Field
from typesystem.json_schema import get_standard_properties

class TestField(Field):
    def __init__(self, has_default_return_value, default_value):
        self._has_default_return_value = has_default_return_value
        self.default = default_value

    def has_default(self):
        return self._has_default_return_value

def test_get_standard_properties_with_default():
    field = TestField(has_default_return_value=True, default_value="default_value")
    result = get_standard_properties(field)
    assert result == {"default": "default_value"}

def test_get_standard_properties_without_default():
    field = TestField(has_default_return_value=False, default_value=None)
    result = get_standard_properties(field)
    assert result == {}
