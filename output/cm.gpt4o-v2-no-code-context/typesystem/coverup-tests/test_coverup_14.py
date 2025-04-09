# file: typesystem/fields.py:68-72
# asked: {"lines": [68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}
# gained: {"lines": [68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}

import pytest
from typesystem.fields import Field

class TestField:
    def test_get_default_value_with_callable_default(self, monkeypatch):
        class TestField(Field):
            def __init__(self):
                self.default = lambda: "callable_default"

        field = TestField()
        assert field.get_default_value() == "callable_default"

    def test_get_default_value_with_non_callable_default(self, monkeypatch):
        class TestField(Field):
            def __init__(self):
                self.default = "non_callable_default"

        field = TestField()
        assert field.get_default_value() == "non_callable_default"

    def test_get_default_value_with_no_default(self, monkeypatch):
        class TestField(Field):
            def __init__(self):
                pass

        field = TestField()
        assert field.get_default_value() is None
