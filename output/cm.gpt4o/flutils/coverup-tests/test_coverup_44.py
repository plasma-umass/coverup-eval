# file flutils/namedtupleutils.py:107-137
# lines [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137]
# branches ['113->114', '113->122', '114->113', '114->115', '120->113', '120->121', '122->123', '122->124', '125->126', '125->129', '129->131', '129->135']

import pytest
from collections import OrderedDict
from collections.abc import Mapping
from typing import Union, Tuple, Any, cast
from flutils.namedtupleutils import _to_namedtuple, NamedTuple

def validate_identifier(identifier: str, allow_underscore: bool = True) -> None:
    if not identifier.isidentifier() or (not allow_underscore and identifier.startswith('_')):
        raise SyntaxError(f"Invalid identifier: {identifier}")

@pytest.fixture
def mock_validate_identifier(mocker):
    return mocker.patch('flutils.namedtupleutils.validate_identifier', side_effect=validate_identifier)

def test_to_namedtuple_with_mapping(mock_validate_identifier):
    data = {
        'validKey': 'value1',
        'anotherValidKey': 'value2',
        'invalid key': 'value3',
        '123invalid': 'value4'
    }
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)
    assert result.validKey == 'value1'
    assert result.anotherValidKey == 'value2'
    assert not hasattr(result, 'invalid key')
    assert not hasattr(result, '123invalid')

def test_to_namedtuple_with_ordered_dict(mock_validate_identifier):
    data = OrderedDict([
        ('validKey', 'value1'),
        ('anotherValidKey', 'value2'),
        ('invalid key', 'value3'),
        ('123invalid', 'value4')
    ])
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)
    assert result.validKey == 'value1'
    assert result.anotherValidKey == 'value2'
    assert not hasattr(result, 'invalid key')
    assert not hasattr(result, '123invalid')

def test_to_namedtuple_with_empty_mapping(mock_validate_identifier):
    data = {}
    result = _to_namedtuple(data)
    assert isinstance(result, tuple)
    assert len(result._fields) == 0
