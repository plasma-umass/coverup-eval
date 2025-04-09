# file: typesystem/json_schema.py:565-569
# asked: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}
# gained: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}

import pytest
from typesystem.fields import Field
from typesystem.json_schema import get_standard_properties

class MockField(Field):
    def __init__(self, has_default, default=None):
        self._has_default = has_default
        self.default = default

    def has_default(self):
        return self._has_default

def test_get_standard_properties_with_default():
    field = MockField(has_default=True, default="default_value")
    result = get_standard_properties(field)
    assert result == {"default": "default_value"}

def test_get_standard_properties_without_default():
    field = MockField(has_default=False)
    result = get_standard_properties(field)
    assert result == {}
