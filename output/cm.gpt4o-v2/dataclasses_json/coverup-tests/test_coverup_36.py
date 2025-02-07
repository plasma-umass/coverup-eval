# file: dataclasses_json/mm.py:278-315
# asked: {"lines": [287, 308], "branches": [[286, 287], [303, 307], [307, 308]]}
# gained: {"lines": [287, 308], "branches": [[286, 287], [307, 308]]}

import pytest
from dataclasses import dataclass, field, MISSING
from dataclasses_json import dataclass_json
from dataclasses_json.mm import schema
from marshmallow import fields as mm_fields
from typing import Optional

@dataclass_json
@dataclass
class TestClass:
    field_with_mm_field: int = field(metadata={'dataclasses_json': {'mm_field': mm_fields.Int()}})
    field_with_letter_case: str = field(metadata={'dataclasses_json': {'letter_case': lambda x: x.upper()}})
    optional_field: Optional[int] = None

def test_schema_with_mm_field():
    result = schema(TestClass, None, False)
    assert 'field_with_mm_field' in result
    assert isinstance(result['field_with_mm_field'], mm_fields.Int)

def test_schema_with_optional_field():
    result = schema(TestClass, None, False)
    assert 'optional_field' in result
    assert result['optional_field'].allow_none is True

def test_schema_with_letter_case():
    result = schema(TestClass, None, False)
    assert 'field_with_letter_case' in result
    assert result['field_with_letter_case'].data_key == 'FIELD_WITH_LETTER_CASE'
