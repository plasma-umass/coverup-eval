# file: lib/ansible/modules/apt_repository.py:485-503
# asked: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}
# gained: {"lines": [487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503], "branches": [[488, 489], [488, 503], [489, 488], [489, 490], [494, 495], [494, 497], [497, 498], [497, 501]]}

import pytest
from unittest.mock import MagicMock

# Assuming the class UbuntuSourcesList and its parent SourcesList are defined in apt_repository module
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_sources_list():
    class MockSourcesList(UbuntuSourcesList):
        def __init__(self, files):
            self.files = files

        def _expand_ppa(self, source_line):
            return "deb http://ppa.launchpad.net/{}/ubuntu {}".format(source_line.split(':')[1], "focal"), "owner", "name"

    return MockSourcesList

def test_repos_urls_valid_enabled(mock_sources_list):
    files = {
        'file1': [
            (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, True, True, 'ppa:some/ppa'),
        ]
    }
    sources_list = mock_sources_list(files)
    repos = sources_list.repos_urls
    assert repos == [
        'deb http://archive.ubuntu.com/ubuntu focal main',
        'deb http://ppa.launchpad.net/some/ppa/ubuntu focal'
    ]

def test_repos_urls_invalid(mock_sources_list):
    files = {
        'file1': [
            (None, False, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, True, False, 'ppa:some/ppa'),
        ]
    }
    sources_list = mock_sources_list(files)
    repos = sources_list.repos_urls
    assert repos == []

def test_repos_urls_mixed(mock_sources_list):
    files = {
        'file1': [
            (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main'),
            (None, False, True, 'deb http://archive.ubuntu.com/ubuntu focal universe'),
            (None, True, False, 'ppa:some/ppa'),
            (None, True, True, 'ppa:another/ppa'),
        ]
    }
    sources_list = mock_sources_list(files)
    repos = sources_list.repos_urls
    assert repos == [
        'deb http://archive.ubuntu.com/ubuntu focal main',
        'deb http://ppa.launchpad.net/another/ppa/ubuntu focal'
    ]
