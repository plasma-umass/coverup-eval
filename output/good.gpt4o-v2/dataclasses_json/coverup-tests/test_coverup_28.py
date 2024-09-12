# file: dataclasses_json/mm.py:216-219
# asked: {"lines": [219], "branches": []}
# gained: {"lines": [219], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import Schema
import typing

class A:
    pass

class JsonData:
    pass

class TestSchemaF:
    def test_loads(self, monkeypatch):
        # Monkeypatch the __init__ method to avoid NotImplementedError
        def mock_init(self, *args, **kwargs):
            pass

        monkeypatch.setattr(SchemaF, "__init__", mock_init)

        schema = SchemaF()
        result = schema.loads(JsonData())
        assert result is None
