# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [], "branches": [[114, 113], [120, 113]]}
# gained: {"lines": [], "branches": [[114, 113]]}

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

def test_to_namedtuple_with_non_identifier_keys(mock_validate_identifier):
    data = {'validKey': 1, 'invalid key': 2}
    result = _to_namedtuple(data)
    assert hasattr(result, 'validKey')
    assert not hasattr(result, 'invalid key')

def test_to_namedtuple_with_non_string_keys(mock_validate_identifier):
    data = {1: 'one', 2: 'two'}
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)
    assert result == ()

def test_to_namedtuple_with_mixed_keys(mock_validate_identifier):
    data = OrderedDict([('validKey', 1), (1, 'one'), ('anotherValidKey', 2)])
    result = _to_namedtuple(data)
    assert hasattr(result, 'validKey')
    assert hasattr(result, 'anotherValidKey')
    assert not hasattr(result, '1')
