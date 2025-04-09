# file lib/ansible/modules/apt_repository.py:485-503
# lines [485, 486, 487, 488, 489, 490, 491, 492, 494, 495, 497, 498, 499, 501, 503]
# branches ['488->489', '488->503', '489->488', '489->490', '494->495', '494->497', '497->498', '497->501']

import pytest
from unittest.mock import MagicMock

# Assuming the UbuntuSourcesList class is part of the apt_repository module
from ansible.modules.apt_repository import UbuntuSourcesList

# Test function to cover the missing branches in UbuntuSourcesList.repos_urls
def test_ubuntu_sources_list_repos_urls(mocker):
    # Mock the apt_pkg module and its config attribute
    apt_pkg_mock = MagicMock()
    mocker.patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock)
    apt_pkg_mock.config.find_file.return_value = '/etc/apt/sources.list'

    # Mock the SourcesList.files attribute to provide test data
    test_files = {
        '/etc/apt/sources.list': [
            (None, True, True, 'deb http://archive.ubuntu.com/ubuntu focal main restricted'),
            (None, False, True, 'deb-src http://archive.ubuntu.com/ubuntu focal main restricted'),  # invalid
            (None, True, False, 'deb http://archive.ubuntu.com/ubuntu focal universe'),  # disabled
            (None, True, True, 'ppa:user/ppa-name')  # PPA
        ]
    }

    # Mock the _expand_ppa method to return a test URL for PPA
    mocker.patch.object(UbuntuSourcesList, '_expand_ppa', return_value=('http://ppa.launchpad.net/user/ppa-name/ubuntu', 'user', 'ppa-name'))

    # Mock the module parameter required by UbuntuSourcesList.__init__
    mock_module = MagicMock()

    # Create an instance of UbuntuSourcesList with the mocked files attribute and module
    ubuntu_sources_list = UbuntuSourcesList(mock_module)
    ubuntu_sources_list.files = test_files

    # Call the repos_urls property and assert the expected results
    expected_repos = [
        'deb http://archive.ubuntu.com/ubuntu focal main restricted',
        'http://ppa.launchpad.net/user/ppa-name/ubuntu'
    ]
    assert ubuntu_sources_list.repos_urls == expected_repos

    # Verify that the _expand_ppa method was called with the correct PPA line
    UbuntuSourcesList._expand_ppa.assert_called_once_with('ppa:user/ppa-name')

    # Clean up by unpatching the mocks
    mocker.stopall()
