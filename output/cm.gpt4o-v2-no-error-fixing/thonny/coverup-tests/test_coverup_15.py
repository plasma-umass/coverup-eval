# file: thonny/jedi_utils.py:138-148
# asked: {"lines": [148], "branches": []}
# gained: {"lines": [148], "branches": []}

import pytest

from thonny.jedi_utils import ThonnyCompletion

def test_thonny_completion_getitem():
    # Arrange
    name = "test_name"
    complete = "test_complete"
    type_ = "test_type"
    description = "test_description"
    parent = "test_parent"
    full_name = "test_full_name"
    
    completion = ThonnyCompletion(name, complete, type_, description, parent, full_name)
    
    # Act & Assert
    assert completion["name"] == name
    assert completion["complete"] == complete
    assert completion["type"] == type_
    assert completion["description"] == description
    assert completion["parent"] == parent
    assert completion["full_name"] == full_name
