# file mimesis/providers/generic.py:66-69
# lines [66, 67, 69]
# branches []

import pytest
from mimesis.providers.generic import Generic

def test_generic_meta_name():
    # Create an instance of the Generic class
    generic_instance = Generic()
    
    # Assert that the Meta class has the correct name attribute
    assert generic_instance.Meta.name == 'generic'
