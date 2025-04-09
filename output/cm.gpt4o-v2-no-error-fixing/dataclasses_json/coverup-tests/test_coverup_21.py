# file: dataclasses_json/mm.py:278-315
# asked: {"lines": [279, 280, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 301, 302, 303, 305, 307, 308, 310, 312, 313, 315], "branches": [[283, 284], [283, 315], [286, 287], [286, 289], [292, 293], [292, 294], [294, 295], [294, 297], [297, 298], [297, 300], [300, 301], [300, 307], [303, 305], [303, 307], [307, 308], [307, 310], [312, 283], [312, 313]]}
# gained: {"lines": [279, 280, 283, 284, 285, 286, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 301, 302, 303, 305, 307, 310, 312, 313, 315], "branches": [[283, 284], [283, 315], [286, 289], [292, 293], [292, 294], [294, 295], [294, 297], [297, 298], [297, 300], [300, 301], [300, 307], [303, 305], [307, 310], [312, 313]]}

import pytest
from dataclasses import dataclass, field, MISSING
from dataclasses_json import dataclass_json
from dataclasses_json.mm import schema
from marshmallow import fields as mm_fields
from typing import Optional, List

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: Optional[str] = None
    c: List[int] = field(default_factory=list)
    d: Optional[int] = field(default=None)
    e: int = field(default=5)
    f: int = field(default_factory=lambda: 10)

def test_schema(monkeypatch):
    def mock_user_overrides_or_exts(cls):
        return {
            'a': {'mm_field': mm_fields.Int()},
            'b': {'mm_field': mm_fields.Str(allow_none=True)},
            'c': {'mm_field': mm_fields.List(mm_fields.Int())},
            'd': {'mm_field': mm_fields.Int(allow_none=True)},
            'e': {'mm_field': mm_fields.Int()},
            'f': {'mm_field': mm_fields.Int()}
        }

    monkeypatch.setattr('dataclasses_json.core._user_overrides_or_exts', mock_user_overrides_or_exts)

    result = schema(TestClass, mixin=None, infer_missing=True)

    assert isinstance(result['a'], mm_fields.Int)
    assert isinstance(result['b'], mm_fields.Str)
    assert result['b'].allow_none is True
    assert isinstance(result['c'], mm_fields.List)
    assert isinstance(result['d'], mm_fields.Int)
    assert result['d'].allow_none is True
    assert isinstance(result['e'], mm_fields.Int)
    assert isinstance(result['f'], mm_fields.Int)

    assert result['e'].missing == 5
    assert result['f'].missing() == 10
