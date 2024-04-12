# file lib/ansible/module_utils/common/collections.py:25-26
# lines [25, 26]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_len(mocker):
    # Mock the _store attribute with a dictionary
    mock_store = mocker.MagicMock()
    mock_store.__len__.return_value = 3

    # Create an instance of ImmutableDict and set the _store attribute
    immutable_dict = ImmutableDict()
    immutable_dict._store = mock_store

    # Assert that __len__ returns the correct length
    assert len(immutable_dict) == 3

    # Verify that the __len__ method of the mock _store was called
    mock_store.__len__.assert_called_once()
