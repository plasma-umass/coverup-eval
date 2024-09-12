# file: flutes/structure.py:99-127
# asked: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}
# gained: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}

import pytest
from flutes.structure import map_structure_zip

def test_map_structure_zip_no_map_types(monkeypatch):
    class NoMapType:
        pass

    def mock_fn(*args):
        return "mocked"

    monkeypatch.setattr("flutes.structure._NO_MAP_TYPES", (NoMapType,))
    result = map_structure_zip(mock_fn, [NoMapType(), NoMapType()])
    assert result == "mocked"

def test_map_structure_zip_no_map_instance_attr(monkeypatch):
    class NoMapInstanceAttr:
        pass

    def mock_fn(*args):
        return "mocked"

    obj = NoMapInstanceAttr()
    setattr(obj, '--no-map--', True)
    result = map_structure_zip(mock_fn, [obj, obj])
    assert result == "mocked"

def test_map_structure_zip_list():
    def mock_fn(*args):
        return sum(args)

    result = map_structure_zip(mock_fn, [[1, 2], [3, 4]])
    assert result == [4, 6]

def test_map_structure_zip_tuple():
    def mock_fn(*args):
        return sum(args)

    result = map_structure_zip(mock_fn, [(1, 2), (3, 4)])
    assert result == (4, 6)

def test_map_structure_zip_namedtuple():
    from collections import namedtuple

    def mock_fn(*args):
        return sum(args)

    Point = namedtuple('Point', ['x', 'y'])
    result = map_structure_zip(mock_fn, [Point(1, 2), Point(3, 4)])
    assert result == Point(4, 6)

def test_map_structure_zip_dict():
    def mock_fn(*args):
        return sum(args)

    result = map_structure_zip(mock_fn, [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
    assert result == {'a': 4, 'b': 6}

def test_map_structure_zip_set():
    def mock_fn(*args):
        return sum(args)

    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(mock_fn, [set([1, 2]), set([3, 4])])
