# file lib/ansible/context.py:38-56
# lines [51, 52, 53, 54, 55]
# branches ['49->51', '51->52', '51->53', '53->54', '53->55']

import pytest
from collections.abc import Mapping, Set
from unittest.mock import MagicMock

# Assuming the CLIARGS is a global variable in the ansible.context module
# We need to import the cliargs_deferred_get function
from ansible.context import cliargs_deferred_get

@pytest.fixture
def mock_cliargs(mocker):
    mock_cliargs = MagicMock()
    mocker.patch('ansible.context.CLIARGS', new=mock_cliargs)
    return mock_cliargs

def test_cliargs_deferred_get_shallowcopy_sequence(mock_cliargs):
    # Setup the CLIARGS to return a list for 'sequence_key'
    mock_cliargs.get.return_value = [1, 2, 3]

    # Get the closure function
    get_sequence = cliargs_deferred_get('sequence_key', shallowcopy=True)

    # Call the closure function
    result = get_sequence()

    # Assert that a shallow copy of the list was returned
    assert result == [1, 2, 3]
    assert result is not mock_cliargs.get.return_value

def test_cliargs_deferred_get_shallowcopy_mapping(mock_cliargs):
    # Setup the CLIARGS to return a dict for 'mapping_key'
    mock_cliargs.get.return_value = {'a': 1, 'b': 2}

    # Get the closure function
    get_mapping = cliargs_deferred_get('mapping_key', shallowcopy=True)

    # Call the closure function
    result = get_mapping()

    # Assert that a shallow copy of the dict was returned
    assert result == {'a': 1, 'b': 2}
    assert result is not mock_cliargs.get.return_value

def test_cliargs_deferred_get_shallowcopy_set(mock_cliargs):
    # Setup the CLIARGS to return a set for 'set_key'
    mock_cliargs.get.return_value = {1, 2, 3}

    # Get the closure function
    get_set = cliargs_deferred_get('set_key', shallowcopy=True)

    # Call the closure function
    result = get_set()

    # Assert that a shallow copy of the set was returned
    assert result == {1, 2, 3}
    assert result is not mock_cliargs.get.return_value
