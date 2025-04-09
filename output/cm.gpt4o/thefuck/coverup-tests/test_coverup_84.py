# file thefuck/shells/generic.py:16-18
# lines [16, 17]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_generic_class_attributes():
    # Verify that the friendly_name attribute is correctly set
    assert Generic.friendly_name == 'Generic Shell'
