# file: lib/ansible/utils/collection_loader/_collection_config.py:100-102
# asked: {"lines": [102], "branches": [[101, 102]]}
# gained: {"lines": [102], "branches": [[101, 102]]}

import pytest
from unittest.mock import patch

# Assuming the class is defined in ansible/utils/collection_loader/_collection_config.py
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_require_finder_not_implemented_error():
    # Ensure the class has the _collection_finder attribute for the test
    with patch.object(_AnsibleCollectionConfig, '_collection_finder', create=True, new=None):
        with pytest.raises(NotImplementedError, match='an AnsibleCollectionFinder has not been installed in this process'):
            _AnsibleCollectionConfig._require_finder(_AnsibleCollectionConfig)
