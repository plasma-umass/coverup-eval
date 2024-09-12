# file: flutes/structure.py:39-46
# asked: {"lines": [39, 46], "branches": []}
# gained: {"lines": [39, 46], "branches": []}

import pytest
from flutes.structure import register_no_map_class

def test_register_no_map_class(monkeypatch):
    # Mock _NO_MAP_TYPES to avoid state pollution
    mock_no_map_types = set()
    monkeypatch.setattr('flutes.structure._NO_MAP_TYPES', mock_no_map_types)

    class CustomContainer:
        pass

    # Register the custom container class
    register_no_map_class(CustomContainer)

    # Assert that the custom container class is now in the _NO_MAP_TYPES set
    assert CustomContainer in mock_no_map_types
