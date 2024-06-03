# file lib/ansible/utils/context_objects.py:20-50
# lines [31, 39, 47]
# branches ['28->31', '36->39', '44->47']

import pytest
from collections.abc import Mapping, Set, Sequence, Container
from ansible.utils.context_objects import _make_immutable, ImmutableDict

def test_make_immutable():
    # Test for line 31: Mapping with non-container value
    input_dict = {'key1': 'value1', 'key2': 42}
    result = _make_immutable(input_dict)
    assert isinstance(result, ImmutableDict)
    assert result['key1'] == 'value1'
    assert result['key2'] == 42

    # Test for line 39: Set with non-container value
    input_set = {'value1', 42}
    result = _make_immutable(input_set)
    assert isinstance(result, frozenset)
    assert 'value1' in result
    assert 42 in result

    # Test for line 47: Sequence with non-container value
    input_list = ['value1', 42]
    result = _make_immutable(input_list)
    assert isinstance(result, tuple)
    assert result[0] == 'value1'
    assert result[1] == 42

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects
    yield
    mocker.stopall()
