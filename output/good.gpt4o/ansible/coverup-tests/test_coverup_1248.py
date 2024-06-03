# file lib/ansible/plugins/loader.py:1148-1157
# lines [1150, 1151]
# branches ['1149->1150']

import pytest
from unittest import mock
from ansible.plugins.loader import _configure_collection_loader, AnsibleCollectionConfig
from ansible.utils.display import Display

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch.object(Display, 'warning')

def test_configure_collection_loader_already_configured(mock_display_warning):
    original_finder = AnsibleCollectionConfig._collection_finder
    try:
        AnsibleCollectionConfig._collection_finder = mock.Mock()
        _configure_collection_loader()
        mock_display_warning.assert_called_once_with('AnsibleCollectionFinder has already been configured')
    finally:
        AnsibleCollectionConfig._collection_finder = original_finder
