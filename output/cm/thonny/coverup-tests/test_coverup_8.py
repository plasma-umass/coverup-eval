# file thonny/jedi_utils.py:138-148
# lines [138, 139, 140, 141, 142, 143, 144, 145, 147, 148]
# branches []

import pytest
from thonny.jedi_utils import ThonnyCompletion

@pytest.fixture
def completion_instance():
    return ThonnyCompletion(
        name="test_name",
        complete="test_complete",
        type="test_type",
        description="test_description",
        parent="test_parent",
        full_name="test_full_name",
    )

def test_thonny_completion_getitem(completion_instance):
    assert completion_instance["name"] == "test_name"
    assert completion_instance["complete"] == "test_complete"
    assert completion_instance["type"] == "test_type"
    assert completion_instance["description"] == "test_description"
    assert completion_instance["parent"] == "test_parent"
    assert completion_instance["full_name"] == "test_full_name"

    with pytest.raises(KeyError):
        completion_instance["non_existent_key"]
