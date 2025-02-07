# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [135, 136, 137], "branches": [[114, 113], [120, 113], [129, 135]]}
# gained: {"lines": [135, 136, 137], "branches": [[114, 113], [129, 135]]}

import pytest
from collections import OrderedDict
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_empty_mapping():
    empty_mapping = OrderedDict()
    result = _to_namedtuple(empty_mapping)
    assert isinstance(result, tuple)
    assert result == ()

def test_to_namedtuple_non_string_key():
    non_string_key_mapping = {123: 'value'}
    result = _to_namedtuple(non_string_key_mapping)
    assert isinstance(result, tuple)
    assert result == ()

def test_to_namedtuple_invalid_identifier(mocker):
    invalid_identifier_mapping = {'123': 'value'}
    mocker.patch('flutils.validators.validate_identifier', side_effect=SyntaxError)
    result = _to_namedtuple(invalid_identifier_mapping)
    assert isinstance(result, tuple)
    assert result == ()
