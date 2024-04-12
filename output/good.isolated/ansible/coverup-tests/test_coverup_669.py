# file lib/ansible/utils/collection_loader/_collection_config.py:100-102
# lines [100, 101, 102]
# branches ['101->exit', '101->102']

import pytest
from ansible.utils.collection_loader import _collection_config

def test_require_finder_without_collection_finder():
    # Create a mock class to test the _require_finder method
    class MockCollectionConfig(metaclass=_collection_config._AnsibleCollectionConfig):
        _collection_finder = None

    # Assert that NotImplementedError is raised when _collection_finder is None
    with pytest.raises(NotImplementedError) as excinfo:
        MockCollectionConfig._require_finder()

    assert str(excinfo.value) == 'an AnsibleCollectionFinder has not been installed in this process'
