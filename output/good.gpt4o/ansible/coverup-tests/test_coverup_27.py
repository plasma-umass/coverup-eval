# file lib/ansible/utils/context_objects.py:20-50
# lines [20, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50]
# branches ['22->24', '22->25', '25->26', '25->33', '27->28', '27->32', '28->29', '28->31', '33->34', '33->41', '35->36', '35->40', '36->37', '36->39', '41->42', '41->50', '43->44', '43->48', '44->45', '44->47']

import pytest
from collections.abc import Mapping, Set, Sequence, Container
from ansible.utils.context_objects import ImmutableDict

def test_make_immutable(mocker):
    # Import the function to be tested
    from ansible.utils.context_objects import _make_immutable

    # Mocking text_type and binary_type
    text_type = str
    binary_type = bytes

    # Test case for text_type
    assert _make_immutable("string") == "string"

    # Test case for binary_type
    assert _make_immutable(b"bytes") == b"bytes"

    # Test case for Mapping
    mock_mapping = mocker.MagicMock(spec=Mapping)
    mock_mapping.items.return_value = [("key", "value")]
    result = _make_immutable(mock_mapping)
    assert isinstance(result, ImmutableDict)
    assert result["key"] == "value"

    # Test case for Set
    mock_set = mocker.MagicMock(spec=Set)
    mock_set.__iter__.return_value = iter(["value"])
    result = _make_immutable(mock_set)
    assert isinstance(result, frozenset)
    assert "value" in result

    # Test case for Sequence
    mock_sequence = mocker.MagicMock(spec=Sequence)
    mock_sequence.__iter__.return_value = iter(["value"])
    result = _make_immutable(mock_sequence)
    assert isinstance(result, tuple)
    assert result[0] == "value"

    # Test case for nested structures
    nested_structure = {
        "key1": ["value1", {"key2": "value2"}],
        "key3": {"key4": {"key5": "value5"}},
        "key6": {"value6"}
    }
    result = _make_immutable(nested_structure)
    assert isinstance(result, ImmutableDict)
    assert isinstance(result["key1"], tuple)
    assert isinstance(result["key1"][1], ImmutableDict)
    assert isinstance(result["key3"], ImmutableDict)
    assert isinstance(result["key3"]["key4"], ImmutableDict)
    assert isinstance(result["key6"], frozenset)

    # Test case for non-container types
    assert _make_immutable(42) == 42
    assert _make_immutable(3.14) == 3.14
    assert _make_immutable(True) == True
