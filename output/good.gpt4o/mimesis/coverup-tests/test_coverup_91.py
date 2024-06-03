# file mimesis/providers/structure.py:32-35
# lines [32, 33, 35]
# branches []

import pytest
from mimesis.providers.structure import Structure

def test_structure_meta():
    # Create an instance of the Structure class
    structure = Structure()
    
    # Verify that the Meta class exists within the Structure class
    assert hasattr(structure, 'Meta')
    
    # Verify that the name attribute in Meta class is 'structure'
    assert structure.Meta.name == 'structure'
