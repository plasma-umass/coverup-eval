# file lib/ansible/utils/collection_loader/_collection_config.py:60-65
# lines [63]
# branches ['62->63']

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_collection_finder_already_configured():
    class TestConfig(metaclass=_AnsibleCollectionConfig):
        _collection_finder = None

    # Set the collection_finder for the first time
    TestConfig.collection_finder = 'first_value'
    
    # Attempt to set the collection_finder again and expect a ValueError
    with pytest.raises(ValueError, match='an AnsibleCollectionFinder has already been configured'):
        TestConfig.collection_finder = 'second_value'
