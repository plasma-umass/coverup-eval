# file: dataclasses_json/mm.py:278-315
# asked: {"lines": [278, 279, 280, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 301, 302, 303, 305, 307, 308, 310, 312, 313, 315], "branches": [[283, 284], [283, 315], [286, 287], [286, 289], [292, 293], [292, 294], [294, 295], [294, 297], [297, 298], [297, 300], [300, 301], [300, 307], [303, 305], [303, 307], [307, 308], [307, 310], [312, 283], [312, 313]]}
# gained: {"lines": [278, 279, 280, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 301, 302, 303, 305, 307, 308, 310, 312, 313, 315], "branches": [[283, 284], [283, 315], [286, 287], [286, 289], [292, 293], [292, 294], [294, 295], [294, 297], [297, 298], [297, 300], [300, 301], [300, 307], [303, 305], [307, 308], [307, 310], [312, 313]]}

import pytest
import typing
from dataclasses import dataclass, field, MISSING
from dataclasses_json import dataclass_json
from dataclasses_json.mm import schema as generate_schema
from unittest.mock import patch

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: str = field(default="default")
    c: int = field(default_factory=lambda: 42)
    d: typing.Optional[str] = None

def test_schema_with_infer_missing_true():
    with patch('dataclasses_json.mm._user_overrides_or_exts', return_value={
        'a': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'b': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'c': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'd': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
    }):
        result = generate_schema(TestClass, mixin=None, infer_missing=True)
        assert 'a' in result
        assert 'b' in result
        assert 'c' in result
        assert 'd' in result

def test_schema_with_infer_missing_false():
    with patch('dataclasses_json.mm._user_overrides_or_exts', return_value={
        'a': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'b': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'c': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'd': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
    }):
        result = generate_schema(TestClass, mixin=None, infer_missing=False)
        assert 'a' in result
        assert 'b' in result
        assert 'c' in result
        assert 'd' in result

def test_schema_with_letter_case():
    with patch('dataclasses_json.mm._user_overrides_or_exts', return_value={
        'a': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': str.upper}),
        'b': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'c': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'd': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
    }):
        result = generate_schema(TestClass, mixin=None, infer_missing=True)
        assert 'a' in result
        assert 'b' in result
        assert 'c' in result
        assert 'd' in result
        assert result['a'].data_key == 'A'

def test_schema_with_mm_field():
    mock_field = type('MockField', (object,), {})()
    with patch('dataclasses_json.mm._user_overrides_or_exts', return_value={
        'a': type('MockMetadata', (object,), {'mm_field': mock_field, 'letter_case': None}),
        'b': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'c': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        'd': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
    }):
        result = generate_schema(TestClass, mixin=None, infer_missing=True)
        assert result['a'] == mock_field
        assert 'b' in result
        assert 'c' in result
        assert 'd' in result
