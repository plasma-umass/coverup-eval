# file flutils/namedtupleutils.py:107-137
# lines []
# branches ['114->113', '120->113']

import pytest
from collections import namedtuple, OrderedDict
from typing import Mapping, NamedTuple, Union, Any, Tuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_non_identifier_keys(mocker):
    # Mock the validate_identifier to raise SyntaxError for non-identifier keys
    mocker.patch('flutils.namedtupleutils.validate_identifier', side_effect=lambda x, **kwargs: x.isidentifier())

    # Create a mapping with non-identifier keys
    non_identifier_keys = {'1invalid': 'value1', 'also invalid': 'value2', 'valid_key': 'value3'}
    ordered_dict = OrderedDict(non_identifier_keys)

    # Call the _to_namedtuple function with the mocked validate_identifier
    result = _to_namedtuple(ordered_dict)

    # Assert that the result only contains the valid identifier key
    assert isinstance(result, tuple)
    assert 'valid_key' in result._fields
    assert len(result._fields) == 1
    assert result.valid_key == 'value3'

    # Assert that the validate_identifier was called for each key
    validate_identifier_mock = mocker.patch('flutils.namedtupleutils.validate_identifier')
    _to_namedtuple(ordered_dict)
    assert validate_identifier_mock.call_count == len(non_identifier_keys)
