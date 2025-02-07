# file: lib/ansible/utils/collection_loader/_collection_config.py:106-107
# asked: {"lines": [106, 107], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

def test_ansible_collection_config_instantiation():
    # Instantiate the class to ensure lines 106-107 are executed
    config = AnsibleCollectionConfig()
    assert config is not None
