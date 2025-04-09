# file: dataclasses_json/mm.py:178-180
# asked: {"lines": [180], "branches": []}
# gained: {"lines": [180], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_dumps(monkeypatch):
    class DummySchema(SchemaF):
        def dumps(self, obj, many=None, *args, **kwargs):
            return super().dumps(obj, many, *args, **kwargs)

    def mock_init(self, *args, **kwargs):
        pass

    monkeypatch.setattr(SchemaF, "__init__", mock_init)

    dummy_schema = DummySchema()
    result = dummy_schema.dumps(obj={})
    assert result is None
