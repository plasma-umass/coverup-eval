# file lib/ansible/utils/context_objects.py:20-50
# lines [22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50]
# branches ['22->24', '22->25', '25->26', '25->33', '27->28', '27->32', '28->29', '28->31', '33->34', '33->41', '35->36', '35->40', '36->37', '36->39', '41->42', '41->50', '43->44', '43->48', '44->45', '44->47']

import pytest
from ansible.utils.context_objects import _make_immutable
from collections.abc import Mapping, Set, Sequence, Container

try:
    from ansible.module_utils.common._collections_compat import ImmutableDict
except ImportError:
    from ansible.module_utils.six.moves.collections_abc import Mapping as ImmutableDict

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_make_immutable(cleanup, mocker):
    # Test with string
    assert _make_immutable("test_string") == "test_string"
    # Test with mapping
    assert isinstance(_make_immutable({'key': 'value'}), ImmutableDict)
    # Test with set
    assert isinstance(_make_immutable({'value1', 'value2'}), frozenset)
    # Test with sequence
    assert isinstance(_make_immutable(['value1', 'value2']), tuple)
    # Test with nested containers
    nested = {'key1': ['value1', {'key2': 'value2'}]}
    immutable_nested = _make_immutable(nested)
    assert isinstance(immutable_nested, ImmutableDict)
    assert isinstance(immutable_nested['key1'], tuple)
    assert isinstance(immutable_nested['key1'][1], ImmutableDict)
    # Test with non-container
    assert _make_immutable(42) == 42
