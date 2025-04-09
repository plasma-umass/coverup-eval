# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [], "branches": [[114, 113], [120, 113]]}
# gained: {"lines": [], "branches": [[114, 113]]}

import pytest
from collections import OrderedDict
from collections.abc import Mapping
from flutils.namedtupleutils import _to_namedtuple
from flutils.validators import validate_identifier

def test_to_namedtuple_with_mapping(monkeypatch):
    class MockValidator:
        def __call__(self, identifier, allow_underscore=True):
            if not identifier.isidentifier():
                raise SyntaxError(f"Invalid identifier: {identifier}")

    monkeypatch.setattr('flutils.validators.validate_identifier', MockValidator())

    # Test with a simple dictionary
    data = {'key1': 'value1', 'key2': 'value2'}
    result = _to_namedtuple(data)
    assert result.key1 == 'value1'
    assert result.key2 == 'value2'

    # Test with an OrderedDict
    ordered_data = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
    result = _to_namedtuple(ordered_data)
    assert result.key1 == 'value1'
    assert result.key2 == 'value2'

    # Test with invalid identifiers
    invalid_data = {'1key': 'value1', 'key-2': 'value2', 'key3': 'value3'}
    result = _to_namedtuple(invalid_data)
    assert hasattr(result, 'key3')
    assert not hasattr(result, '1key')
    assert not hasattr(result, 'key-2')

    # Test with nested dictionary
    nested_data = {'key1': {'subkey1': 'subvalue1'}, 'key2': 'value2'}
    result = _to_namedtuple(nested_data)
    assert result.key1.subkey1 == 'subvalue1'
    assert result.key2 == 'value2'

    # Test with empty dictionary
    empty_data = {}
    result = _to_namedtuple(empty_data)
    assert result == ()

    # Test with non-string keys
    non_string_keys = {1: 'value1', (2, 3): 'value2', 'key3': 'value3'}
    result = _to_namedtuple(non_string_keys)
    assert result.key3 == 'value3'
    assert not hasattr(result, '1')
    assert not hasattr(result, '(2, 3)')
