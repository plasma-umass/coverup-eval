# file lib/ansible/utils/collection_loader/_collection_config.py:106-107
# lines [106, 107]
# branches []

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig
from ansible.utils.collection_loader._collection_config import with_metaclass

def test_ansible_collection_config(mocker):
    # Mock the metaclass to ensure it is called
    mock_metaclass = mocker.patch('ansible.utils.collection_loader._collection_config._AnsibleCollectionConfig', autospec=True)

    # Define the class within the test to ensure it gets executed
    class AnsibleCollectionConfig(with_metaclass(mock_metaclass)):
        pass

    # Assert that the metaclass was called
    mock_metaclass.assert_called_once()

    # Clean up by deleting the class
    del AnsibleCollectionConfig
