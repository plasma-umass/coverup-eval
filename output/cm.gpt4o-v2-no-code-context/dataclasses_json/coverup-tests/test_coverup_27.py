# file: dataclasses_json/mm.py:165-167
# asked: {"lines": [167], "branches": []}
# gained: {"lines": [167], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_dump(monkeypatch):
    class DummySchema(SchemaF):
        def dump(self, obj, many=None):
            return super().dump(obj, many)

    def mock_init(self, *args, **kwargs):
        pass

    monkeypatch.setattr(SchemaF, "__init__", mock_init)

    dummy_schema = DummySchema()
    result = dummy_schema.dump(obj="test", many=False)
    assert result is None
