# file lib/ansible/playbook/collectionsearch.py:34-61
# lines [34, 37, 38, 40, 43, 46, 48, 49, 55, 56, 57, 58, 59, 61]
# branches ['48->49', '48->55', '56->57', '56->61', '57->56', '57->58']

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.collectionsearch import CollectionSearch

@pytest.fixture
def collection_search():
    class MockCollectionSearch(CollectionSearch):
        def get_validated_value(self, name, field, value, default):
            return value

    return MockCollectionSearch()

def test_load_collections_empty(collection_search):
    ds = []
    result = collection_search._load_collections('collections', ds)
    assert result is None

def test_load_collections_with_values(collection_search):
    ds = ['community.general', 'ansible.builtin']
    with patch('ansible.playbook.collectionsearch._ensure_default_collection') as mock_ensure_default_collection:
        result = collection_search._load_collections('collections', ds)
        mock_ensure_default_collection.assert_called_once_with(collection_list=ds)
        assert result == ds

def test_load_collections_with_template_warning(collection_search, mocker):
    ds = ['{{ templated_collection }}', 'ansible.legacy']
    mocker.patch('ansible.playbook.collectionsearch.is_template', side_effect=[True, False])
    mocker.patch('ansible.playbook.collectionsearch.Environment', return_value=MagicMock())
    mock_display_warning = mocker.patch('ansible.playbook.collectionsearch.display.warning')

    result = collection_search._load_collections('collections', ds)
    mock_display_warning.assert_called_once_with('"collections" is not templatable, but we found: {{ templated_collection }}, '
                                                 'it will not be templated and will be used "as is".')
    assert result == ds
