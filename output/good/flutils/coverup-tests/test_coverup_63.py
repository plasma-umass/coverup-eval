# file flutils/namedtupleutils.py:107-137
# lines [118, 119, 135, 136, 137]
# branches ['114->113', '120->113', '122->124', '129->135']

import pytest
from collections import namedtuple, OrderedDict
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_coverage(mocker):
    # Mock validate_identifier to raise SyntaxError for '1invalid' and pass for 'valid'
    def side_effect_validate_identifier(value, allow_underscore):
        if value == '1invalid':
            raise SyntaxError
        else:
            return None

    mocker.patch('flutils.namedtupleutils.validate_identifier', side_effect=side_effect_validate_identifier)

    # Test that invalid identifiers are skipped
    invalid_dict = {'1invalid': 'value', 'valid': 'value'}
    result = _to_namedtuple(invalid_dict)
    assert isinstance(result, tuple) and hasattr(result, '_fields')
    assert 'valid' in result._fields
    assert '1invalid' not in result._fields

    # Test that non-OrderedDict is sorted
    unsorted_dict = {'b': 1, 'a': 2}
    result = _to_namedtuple(unsorted_dict)
    assert result._fields == ('a', 'b')

    # Test that OrderedDict is not sorted
    ordered_dict = OrderedDict([('b', 1), ('a', 2)])
    result = _to_namedtuple(ordered_dict)
    assert result._fields == ('b', 'a')

    # Test that an empty mapping returns an empty namedtuple
    empty_dict = {}
    result = _to_namedtuple(empty_dict)
    assert isinstance(result, tuple) and hasattr(result, '_fields')
    assert result._fields == ()

    # Cleanup mock
    mocker.stopall()
