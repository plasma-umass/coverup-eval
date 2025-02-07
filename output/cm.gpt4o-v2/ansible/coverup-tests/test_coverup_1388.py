# file: lib/ansible/modules/apt_repository.py:478-483
# asked: {"lines": [479, 480, 482, 483], "branches": [[479, 480], [479, 482]]}
# gained: {"lines": [479, 480, 482, 483], "branches": [[479, 480], [479, 482]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def ubuntu_sources_list():
    module = MagicMock()
    module.params = {'codename': 'focal'}
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt_pkg:
        mock_apt_pkg.config.find_file.return_value = '/dev/null'
        return UbuntuSourcesList(module)

def test_remove_source_with_ppa(ubuntu_sources_list):
    line = 'ppa:some/ppa'
    expanded_ppa = ['deb http://ppa.launchpad.net/some/ppa/ubuntu focal main']
    
    with patch.object(UbuntuSourcesList, '_expand_ppa', return_value=expanded_ppa) as mock_expand_ppa, \
         patch.object(UbuntuSourcesList, '_remove_valid_source') as mock_remove_valid_source:
        
        ubuntu_sources_list.remove_source(line)
        
        mock_expand_ppa.assert_called_once_with(line)
        mock_remove_valid_source.assert_called_once_with(expanded_ppa[0])

def test_remove_source_with_non_ppa(ubuntu_sources_list):
    line = 'deb http://archive.ubuntu.com/ubuntu focal main'
    parsed_source = [None, None, 'deb http://archive.ubuntu.com/ubuntu focal main']
    
    with patch.object(UbuntuSourcesList, '_parse', return_value=parsed_source) as mock_parse, \
         patch.object(UbuntuSourcesList, '_remove_valid_source') as mock_remove_valid_source:
        
        ubuntu_sources_list.remove_source(line)
        
        mock_parse.assert_called_once_with(line, raise_if_invalid_or_disabled=True)
        mock_remove_valid_source.assert_called_once_with(parsed_source[2])
