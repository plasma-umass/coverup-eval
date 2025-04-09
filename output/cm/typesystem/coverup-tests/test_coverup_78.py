# file typesystem/json_schema.py:352-355
# lines [353, 354, 355]
# branches []

import pytest
from typesystem.fields import Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import from_json_schema, AllOf

@pytest.fixture
def cleanup_definitions():
    # Setup: Create a definitions instance if needed
    definitions = SchemaDefinitions()
    yield definitions
    # Teardown: Clean up any changes to the definitions if necessary

def test_all_of_from_json_schema(cleanup_definitions):
    definitions = cleanup_definitions
    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    
    result = from_json_schema(data, definitions=definitions)
    
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert isinstance(result.all_of[0], Field)
    assert isinstance(result.all_of[1], Field)
    assert result.default == "default_value"
