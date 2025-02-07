# file: dataclasses_json/mm.py:190-194
# asked: {"lines": [190, 191, 192, 193, 194], "branches": []}
# gained: {"lines": [190, 191, 192, 193], "branches": []}

import pytest
from marshmallow import Schema
import typing
from dataclasses_json.mm import SchemaF

class A:
    pass

class TEncoded:
    pass

class TOneOrMultiEncoded:
    pass

class TOneOrMulti:
    pass

class JsonData:
    pass

class TestSchemaF:
    def test_load_overload(self, monkeypatch):
        class TestSchema(SchemaF[A]):
            def __init__(self, *args, **kwargs):
                pass

        schema = TestSchema()
        data = TEncoded()
        
        with monkeypatch.context() as m:
            m.setattr(SchemaF, '__init__', lambda *args, **kwargs: None)
            schema = TestSchema()
            result = schema.load(data, many=None, partial=None, unknown=None)
            assert result is None

    def test_load_overload_list(self, monkeypatch):
        class TestSchema(SchemaF[A]):
            def __init__(self, *args, **kwargs):
                pass

        schema = TestSchema()
        data = [TEncoded()]
        
        with monkeypatch.context() as m:
            m.setattr(SchemaF, '__init__', lambda *args, **kwargs: None)
            schema = TestSchema()
            result = schema.load(data, many=True, partial=None, unknown=None)
            assert result is None
