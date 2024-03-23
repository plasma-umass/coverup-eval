# file mimesis/providers/structure.py:32-35
# lines [32, 33, 35]
# branches []

import pytest
from mimesis.providers.structure import Structure

def test_structure_meta_name():
    structure = Structure()
    assert structure.Meta.name == 'structure'
