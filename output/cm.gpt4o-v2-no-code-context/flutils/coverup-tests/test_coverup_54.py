# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 113], [114, 115], [120, 113], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}
# gained: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 115], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}

import pytest
from collections import OrderedDict
from collections.abc import Mapping
from typing import NamedTuple, Union, Tuple, Any, cast
from flutils.namedtupleutils import _to_namedtuple

def validate_identifier(identifier: str, allow_underscore: bool = True) -> None:
    if not identifier.isidentifier() or (not allow_underscore and identifier.startswith('_')):
        raise SyntaxError(f"Invalid identifier: {identifier}")

@pytest.fixture
def mock_validate_identifier(monkeypatch):
    def mock_validate_identifier(identifier: str, allow_underscore: bool = True) -> None:
        if not identifier.isidentifier() or (not allow_underscore and identifier.startswith('_')):
            raise SyntaxError(f"Invalid identifier: {identifier}")
    monkeypatch.setattr('flutils.namedtupleutils.validate_identifier', mock_validate_identifier)

def test_to_namedtuple_with_mapping(mock_validate_identifier):
    data = {
        'validKey1': 1,
        'validKey2': 2,
        'invalid key': 3,
        'anotherInvalidKey!': 4
    }
    result = _to_namedtuple(data)
    assert hasattr(result, 'validKey1')
    assert hasattr(result, 'validKey2')
    assert result.validKey1 == 1
    assert result.validKey2 == 2
    with pytest.raises(AttributeError):
        _ = result.invalid_key
    with pytest.raises(AttributeError):
        _ = result.anotherInvalidKey

def test_to_namedtuple_with_ordered_dict(mock_validate_identifier):
    data = OrderedDict([
        ('validKey1', 1),
        ('validKey2', 2),
        ('invalid key', 3),
        ('anotherInvalidKey!', 4)
    ])
    result = _to_namedtuple(data)
    assert hasattr(result, 'validKey1')
    assert hasattr(result, 'validKey2')
    assert result.validKey1 == 1
    assert result.validKey2 == 2
    with pytest.raises(AttributeError):
        _ = result.invalid_key
    with pytest.raises(AttributeError):
        _ = result.anotherInvalidKey

def test_to_namedtuple_with_empty_mapping(mock_validate_identifier):
    data = {}
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)
    assert not hasattr(result, 'validKey1')
    assert not hasattr(result, 'validKey2')
