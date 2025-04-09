# file lib/ansible/utils/collection_loader/_collection_config.py:51-54
# lines [51, 52, 53, 54]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_config

# Assuming the _EventSource class is defined somewhere within the ansible.utils.collection_loader module
# If it's not, you would need to import it from the correct location or mock it if it's external

class TestAnsibleCollectionConfig:
    def test_ansible_collection_config_initialization(self, mocker):
        # Mock the _EventSource to ensure it does not have side effects
        mock_event_source = mocker.patch('ansible.utils.collection_loader._collection_config._EventSource')

        # Define a subclass to trigger the __init__ method of the metaclass
        class TestCollection(metaclass=_collection_config._AnsibleCollectionConfig):
            pass

        # Assertions to check postconditions (if any)
        assert TestCollection._collection_finder is None
        assert TestCollection._default_collection is None
        assert mock_event_source.called_once()

        # No cleanup is necessary as we are not modifying any global state
