# file lib/ansible/modules/apt_repository.py:443-452
# lines [444, 445, 446, 447, 448, 449, 451, 452]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the UbuntuSourcesList class is part of the apt_repository module
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def ubuntu_sources_list(mocker):
    mock_codename = 'focal'
    mock_module = MagicMock()
    with patch('ansible.modules.apt_repository.apt_pkg', create=True):
        ubuntu_sources = UbuntuSourcesList(mock_module)
        ubuntu_sources.codename = mock_codename
    return ubuntu_sources

def test_expand_ppa_with_only_owner(ubuntu_sources_list):
    # Mocking the path to simulate a PPA with only the owner part
    path = "ppa:someowner"
    
    # Call the method under test
    line, ppa_owner, ppa_name = ubuntu_sources_list._expand_ppa(path)
    
    # Assertions to check if the line, ppa_owner, and ppa_name are correct
    assert ppa_owner == 'someowner'
    assert ppa_name == 'ppa'
    assert line == 'deb http://ppa.launchpad.net/someowner/ppa/ubuntu focal main'
