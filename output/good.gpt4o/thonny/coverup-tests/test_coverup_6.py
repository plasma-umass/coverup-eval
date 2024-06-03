# file thonny/jedi_utils.py:138-148
# lines [138, 139, 140, 141, 142, 143, 144, 145, 147, 148]
# branches []

import pytest
from thonny.jedi_utils import ThonnyCompletion

def test_thonny_completion():
    # Create an instance of ThonnyCompletion
    completion = ThonnyCompletion(
        name="test_name",
        complete="test_complete",
        type="test_type",
        description="test_description",
        parent="test_parent",
        full_name="test_full_name"
    )
    
    # Verify the attributes are set correctly
    assert completion.name == "test_name"
    assert completion.complete == "test_complete"
    assert completion.type == "test_type"
    assert completion.description == "test_description"
    assert completion.parent == "test_parent"
    assert completion.full_name == "test_full_name"
    
    # Test __getitem__ method
    assert completion["name"] == "test_name"
    assert completion["complete"] == "test_complete"
    assert completion["type"] == "test_type"
    assert completion["description"] == "test_description"
    assert completion["parent"] == "test_parent"
    assert completion["full_name"] == "test_full_name"
