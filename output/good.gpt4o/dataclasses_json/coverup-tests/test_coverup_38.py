# file dataclasses_json/mm.py:278-315
# lines [279, 280, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 301, 302, 303, 305, 307, 308, 310, 312, 313, 315]
# branches ['283->284', '283->315', '286->287', '286->289', '292->293', '292->294', '294->295', '294->297', '297->298', '297->300', '300->301', '300->307', '303->305', '303->307', '307->308', '307->310', '312->283', '312->313']

import pytest
from dataclasses import dataclass, field, MISSING
from dataclasses_json.mm import schema as generate_schema
from dataclasses_json import dataclass_json
from unittest.mock import patch
import typing

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: str = field(default="default_b")
    c: float = field(default_factory=lambda: 1.23)
    d: typing.Optional[int] = None

def test_schema_generation():
    with patch('dataclasses_json.mm._user_overrides_or_exts') as mock_overrides:
        mock_overrides.return_value = {
            'a': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
            'b': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
            'c': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
            'd': type('MockMetadata', (object,), {'mm_field': None, 'letter_case': None}),
        }
        
        schema = generate_schema(TestClass, mixin=None, infer_missing=True)
        
        assert 'a' in schema
        assert 'b' in schema
        assert 'c' in schema
        assert 'd' in schema
        assert schema['b'].missing == "default_b"
        assert schema['c'].missing() == 1.23
        assert schema['d'].allow_none is True
        assert schema['d'].missing is None
