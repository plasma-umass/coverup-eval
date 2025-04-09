# file: lib/ansible/utils/collection_loader/_collection_config.py:106-107
# asked: {"lines": [106, 107], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from ansible.module_utils.six import with_metaclass
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_ansible_collection_config_instantiation():
    class AnsibleCollectionConfig(with_metaclass(_AnsibleCollectionConfig)):
        pass

    # Instantiate the class to ensure lines 106-107 are executed
    config = AnsibleCollectionConfig()
    assert config is not None
