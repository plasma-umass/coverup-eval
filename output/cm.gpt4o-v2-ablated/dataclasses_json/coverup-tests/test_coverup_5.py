# file: dataclasses_json/mm.py:146-153
# asked: {"lines": [146, 152, 153], "branches": []}
# gained: {"lines": [146, 152, 153], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import Schema

def test_schemaf_not_implemented_error():
    with pytest.raises(NotImplementedError):
        SchemaF()

def test_schemaf_inheritance_not_allowed():
    class InheritedSchemaF(SchemaF):
        pass

    with pytest.raises(NotImplementedError):
        InheritedSchemaF()

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Ensure no state pollution
