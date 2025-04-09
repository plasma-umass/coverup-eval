# file: lib/ansible/utils/collection_loader/_collection_config.py:106-107
# asked: {"lines": [106, 107], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig
from ansible.module_utils.six import with_metaclass

def test_ansible_collection_config_class():
    class AnsibleCollectionConfig(with_metaclass(_AnsibleCollectionConfig, object)):
        pass

    # Verify that the class is created and is an instance of _AnsibleCollectionConfig
    assert isinstance(AnsibleCollectionConfig(), AnsibleCollectionConfig)
