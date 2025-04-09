# file lib/ansible/utils/collection_loader/_collection_config.py:60-65
# lines [60, 61, 62, 63, 65]
# branches ['62->63', '62->65']

import pytest
from ansible.utils.collection_loader import _collection_config

def test_collection_finder_setter_once(mocker):
    # Mock the _AnsibleCollectionConfig class
    mock_cls = mocker.MagicMock()
    mock_cls._collection_finder = None

    # Set the collection_finder for the first time
    _collection_config._AnsibleCollectionConfig.collection_finder.fset(mock_cls, 'finder')

    # Assert that the collection_finder was set
    assert mock_cls._collection_finder == 'finder'

    # Attempt to set the collection_finder a second time and expect a ValueError
    with pytest.raises(ValueError) as excinfo:
        _collection_config._AnsibleCollectionConfig.collection_finder.fset(mock_cls, 'another_finder')

    # Assert that the exception message is correct
    assert str(excinfo.value) == 'an AnsibleCollectionFinder has already been configured'

    # Clean up by resetting the _collection_finder to None
    mock_cls._collection_finder = None
