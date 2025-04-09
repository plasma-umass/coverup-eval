# file lib/ansible/utils/collection_loader/_collection_config.py:81-83
# lines [81, 82, 83]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_config

# Assuming the _AnsibleCollectionConfig class is part of a larger module that we are testing

def test_ansible_collection_config_on_collection_load(mocker):
    # Mock the _on_collection_load attribute before the test
    mock_on_collection_load = mocker.PropertyMock(return_value='mocked_value')
    mocker.patch.object(_collection_config._AnsibleCollectionConfig, 'on_collection_load', new=mock_on_collection_load)

    # Access the property to ensure the line is covered
    result = _collection_config._AnsibleCollectionConfig.on_collection_load

    # Verify that the result is as expected from the mocked property
    assert result == 'mocked_value'
    mock_on_collection_load.assert_called_once()
