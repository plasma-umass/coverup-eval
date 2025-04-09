# file src/blib2to3/pytree.py:170-175
# lines [172]
# branches ['171->172']

import pytest
from unittest.mock import Mock

# Assuming the Base class is imported from blib2to3.pytree
from blib2to3.pytree import Base

class TestBase(Base):
    def __init__(self):
        self.was_changed = False
        self.parent = None

def test_changed_line_172():
    # Create a mock parent object
    mock_parent = Mock(spec=Base)
    
    # Create an instance of TestBase and set up the conditions to hit line 172
    base_instance = TestBase()
    base_instance.was_changed = True
    base_instance.parent = mock_parent
    
    # Call the changed method
    base_instance.changed()
    
    # Assert that the method returns early and does not call parent.changed()
    mock_parent.changed.assert_not_called()
    assert base_instance.was_changed is True
