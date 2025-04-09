# file src/blib2to3/pytree.py:170-175
# lines [172]
# branches ['171->172']

import pytest
from blib2to3.pytree import Base

class Derived(Base):
    def __init__(self):
        super(Derived, self).__init__()
        self.was_changed = False
        self.parent = None

def test_base_changed_already_changed(mocker):
    # Create a derived instance and set was_changed to True
    derived_instance = Derived()
    derived_instance.was_changed = True

    # Mock the parent's changed method to ensure it's not called
    mock_parent = mocker.Mock(spec=Base)
    derived_instance.parent = mock_parent

    # Call the changed method on the derived instance
    derived_instance.changed()

    # Assert that the parent's changed method was not called
    mock_parent.changed.assert_not_called()

    # Assert that was_changed remains True
    assert derived_instance.was_changed is True
