# file: lib/ansible/modules/apt_repository.py:485-503
# asked: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}
# gained: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the necessary imports for UbuntuSourcesList and SourcesList are already in place
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def ubuntu_sources_list():
    module = MagicMock()
    module.params = {'codename': 'focal'}
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt_pkg:
        mock_apt_pkg.config.find_file.return_value = '/dev/null'
        return UbuntuSourcesList(module)

def test_repos_urls_with_valid_and_enabled_repos(ubuntu_sources_list):
    ubuntu_sources_list.files = {
        'file1': [
            (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, True, True, 'ppa:some/ppa'),
        ]
    }
    
    ubuntu_sources_list._expand_ppa = MagicMock(return_value=('deb http://ppa.launchpad.net/some/ppa/ubuntu focal main', 'some', 'ppa'))
    
    repos = ubuntu_sources_list.repos_urls
    
    assert repos == [
        'deb http://archive.ubuntu.com/ubuntu focal main',
        'deb http://ppa.launchpad.net/some/ppa/ubuntu focal main'
    ]

def test_repos_urls_with_invalid_or_disabled_repos(ubuntu_sources_list):
    ubuntu_sources_list.files = {
        'file1': [
            (None, False, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, True, False, 'deb http://archive.ubuntu.com/ubuntu focal universe'),
            (None, False, False, 'ppa:some/ppa'),
        ]
    }
    
    repos = ubuntu_sources_list.repos_urls
    
    assert repos == []

def test_repos_urls_with_mixed_repos(ubuntu_sources_list):
    ubuntu_sources_list.files = {
        'file1': [
            (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, False, True, 'deb http://archive.ubuntu.com/ubuntu focal universe'),
            (None, True, False, 'ppa:some/ppa'),
            (None, True, True, 'ppa:another/ppa'),
        ]
    }
    
    ubuntu_sources_list._expand_ppa = MagicMock(return_value=('deb http://ppa.launchpad.net/another/ppa/ubuntu focal main', 'another', 'ppa'))
    
    repos = ubuntu_sources_list.repos_urls
    
    assert repos == [
        'deb http://archive.ubuntu.com/ubuntu focal main',
        'deb http://ppa.launchpad.net/another/ppa/ubuntu focal main'
    ]
