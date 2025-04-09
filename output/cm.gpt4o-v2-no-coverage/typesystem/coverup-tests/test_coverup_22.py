# file: typesystem/json_schema.py:565-569
# asked: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}
# gained: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}

import pytest
from typesystem.fields import Field
from typesystem.json_schema import get_standard_properties

def test_get_standard_properties_with_default():
    field = Field(default="test_default")
    result = get_standard_properties(field)
    assert result == {"default": "test_default"}

def test_get_standard_properties_without_default():
    field = Field()
    result = get_standard_properties(field)
    assert result == {}
