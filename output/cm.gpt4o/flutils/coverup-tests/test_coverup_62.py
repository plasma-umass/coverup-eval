# file flutils/namedtupleutils.py:107-137
# lines []
# branches ['114->113', '120->113']

import pytest
from collections import OrderedDict
from collections.abc import Mapping
from typing import NamedTuple, Union, Tuple, Any, cast
from flutils.namedtupleutils import _to_namedtuple

def validate_identifier(identifier: str, allow_underscore: bool = True) -> None:
    if not identifier.isidentifier() or (not allow_underscore and identifier.startswith('_')):
        raise SyntaxError(f"Invalid identifier: {identifier}")

@pytest.fixture
def mock_validate_identifier(mocker):
    return mocker.patch('flutils.namedtupleutils.validate_identifier', side_effect=validate_identifier)

def test_to_namedtuple_with_non_identifier_keys(mock_validate_identifier):
    data = {
        'validKey': 'value1',
        'invalid key': 'value2',  # This should trigger the SyntaxError and be skipped
        'anotherValidKey': 'value3'
    }
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)  # Corrected to check for tuple instead of NamedTuple
    assert hasattr(result, 'validKey')
    assert hasattr(result, 'anotherValidKey')
    assert not hasattr(result, 'invalid key')
    assert result.validKey == 'value1'
    assert result.anotherValidKey == 'value3'

def test_to_namedtuple_with_non_string_keys(mock_validate_identifier):
    data = {
        123: 'value1',  # This should be skipped because the key is not a string
        'validKey': 'value2'
    }
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)  # Corrected to check for tuple instead of NamedTuple
    assert hasattr(result, 'validKey')
    assert not hasattr(result, '123')
    assert result.validKey == 'value2'
