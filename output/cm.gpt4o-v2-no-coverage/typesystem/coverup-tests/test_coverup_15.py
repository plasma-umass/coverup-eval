# file: typesystem/fields.py:68-72
# asked: {"lines": [68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}
# gained: {"lines": [68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}

import pytest
from typesystem.fields import Field

def test_get_default_value_with_none():
    field = Field()
    assert field.get_default_value() is None

def test_get_default_value_with_non_callable():
    field = Field()
    field.default = 42
    assert field.get_default_value() == 42

def test_get_default_value_with_callable():
    field = Field()
    field.default = lambda: 42
    assert field.get_default_value() == 42
