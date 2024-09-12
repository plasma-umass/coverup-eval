# file: flutes/structure.py:74-96
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest
from flutes.structure import map_structure

class NoMapType:
    pass

def test_map_structure_no_map_type(monkeypatch):
    obj = NoMapType()
    fn = lambda x: x

    # Mock _NO_MAP_TYPES to include NoMapType
    monkeypatch.setattr('flutes.structure._NO_MAP_TYPES', (NoMapType,))
    result = map_structure(fn, obj)
    assert result == obj

def test_map_structure_no_map_instance_attr():
    class CustomClass:
        __no_map__ = True
        def __init__(self, value):
            self.value = value

    obj = CustomClass(10)
    fn = lambda x: x.value if hasattr(x, 'value') else x
    result = map_structure(fn, obj)
    assert result == 10
