# file dataclasses_json/mm.py:146-153
# lines [146, 152, 153]
# branches []

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import Schema

def test_schemaf_not_implemented_error():
    with pytest.raises(NotImplementedError):
        SchemaF()
