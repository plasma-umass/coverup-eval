# file: typesystem/fields.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from typesystem.fields import Field

class TestField:
    def test_has_default_true(self):
        field = Field()
        field.default = "some_default_value"
        assert field.has_default() is True

    def test_has_default_false(self):
        field = Field()
        assert field.has_default() is False
