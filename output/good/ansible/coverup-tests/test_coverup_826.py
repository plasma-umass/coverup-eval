# file lib/ansible/modules/apt_repository.py:413-415
# lines [413, 414, 415]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import SourcesList

class TestSourcesList:

    @pytest.fixture
    def sources_list(self, mocker):
        mocker.patch('ansible.modules.apt_repository.open', mocker.mock_open(read_data='deb http://example.com/ stable main'))
        module_mock = MagicMock()
        with patch('ansible.modules.apt_repository.apt_pkg', create=True) as mock_apt_pkg:
            mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
            return SourcesList(module=module_mock)

    def test_remove_source(self, sources_list, mocker):
        # Mock the internal methods that are not the focus of this test
        mocker.patch.object(sources_list, '_parse', return_value=(None, None, 'deb http://example.com/ stable main'))
        mocker.patch.object(sources_list, '_remove_valid_source')

        # Call the method under test
        sources_list.remove_source('deb http://example.com/ stable main')

        # Assert that the internal methods were called with the expected arguments
        sources_list._parse.assert_called_once_with('deb http://example.com/ stable main', raise_if_invalid_or_disabled=True)
        sources_list._remove_valid_source.assert_called_once_with('deb http://example.com/ stable main')

        # Clean up
        mocker.stopall()
