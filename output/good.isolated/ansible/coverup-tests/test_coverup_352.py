# file lib/ansible/modules/apt_repository.py:196-209
# lines [196, 197, 198, 200, 201, 204, 205, 208, 209]
# branches ['204->205', '204->208', '208->exit', '208->209']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import SourcesList

class TestSourcesList:
    @pytest.fixture
    def mock_module(self):
        module = MagicMock()
        module.params = {'repo': 'deb http://example.com/ubuntu main'}
        return module

    @pytest.fixture
    def mock_os_path(self, mocker):
        mocker.patch('os.path.isfile', return_value=True)
        mocker.patch('glob.iglob', return_value=iter(['test1.list', 'test2.list']))
        return os.path

    @pytest.fixture
    def mock_load(self, mocker):
        mocker.patch.object(SourcesList, 'load', return_value=None)

    @pytest.fixture
    def mock_apt_pkg_config(self, mocker):
        apt_pkg_mock = MagicMock()
        apt_pkg_mock.config.find_file.return_value = '/etc/apt/sources.list'
        mocker.patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock)
        return apt_pkg_mock

    def test_sources_list_init(self, mock_module, mock_os_path, mock_load, mock_apt_pkg_config):
        sources_list = SourcesList(mock_module)
        assert sources_list.default_file == '/etc/apt/sources.list'
        assert sources_list.files == {}
        assert sources_list.new_repos == set()
        sources_list.load.assert_any_call(sources_list.default_file)
        sources_list.load.assert_any_call('test1.list')
        sources_list.load.assert_any_call('test2.list')
        assert sources_list.load.call_count == 3

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])
