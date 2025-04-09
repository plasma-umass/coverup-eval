# file: lib/ansible/modules/apt_repository.py:485-503
# asked: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}
# gained: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import UbuntuSourcesList

class TestUbuntuSourcesList:
    
    @pytest.fixture
    def ubuntu_sources_list(self, mocker):
        mocker.patch('ansible.modules.apt_repository.SourcesList.__init__', return_value=None)
        mocker.patch('ansible.modules.apt_repository.SourcesList.load', return_value=None)
        mocker.patch('ansible.modules.apt_repository.SourcesList._apt_cfg_file', return_value='/etc/apt/sources.list')
        mocker.patch('ansible.modules.apt_repository.SourcesList._apt_cfg_dir', return_value='/etc/apt/sources.list.d')
        module_mock = MagicMock()
        module_mock.params = {'codename': 'focal'}
        usl = UbuntuSourcesList(module=module_mock)
        usl.files = {
            '/etc/apt/sources.list': [
                (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main restricted'),
                (None, True, False, 'deb http://archive.ubuntu.com/ubuntu focal-updates main restricted'),
                (None, False, True, 'deb http://archive.ubuntu.com/ubuntu focal universe'),
                (None, True, True, 'ppa:some/ppa')
            ]
        }
        usl.codename = 'focal'
        return usl

    def test_repos_urls(self, ubuntu_sources_list):
        expected_repos = [
            'deb http://archive.ubuntu.com/ubuntu focal main restricted',
            'deb http://ppa.launchpad.net/some/ppa/ubuntu focal main'
        ]
        assert ubuntu_sources_list.repos_urls == expected_repos
