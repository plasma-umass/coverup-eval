# file: lib/ansible/modules/apt_repository.py:422-426
# asked: {"lines": [422, 423, 424, 425, 426], "branches": []}
# gained: {"lines": [422, 423, 424, 425, 426], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.apt_repository import UbuntuSourcesList, SourcesList, distro, apt_pkg

class TestUbuntuSourcesList:
    
    @patch('ansible.modules.apt_repository.distro')
    @patch('ansible.modules.apt_repository.apt_pkg')
    def test_init_with_codename(self, mock_apt_pkg, mock_distro):
        mock_module = Mock()
        mock_module.params = {'codename': 'focal'}
        mock_distro.codename = 'bionic'
        mock_apt_pkg.config = Mock()
        mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
        
        usl = UbuntuSourcesList(mock_module)
        
        assert usl.module == mock_module
        assert usl.add_ppa_signing_keys_callback is None
        assert usl.codename == 'focal'
    
    @patch('ansible.modules.apt_repository.distro')
    @patch('ansible.modules.apt_repository.apt_pkg')
    def test_init_without_codename(self, mock_apt_pkg, mock_distro):
        mock_module = Mock()
        mock_module.params = {'codename': None}
        mock_distro.codename = 'bionic'
        mock_apt_pkg.config = Mock()
        mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
        
        usl = UbuntuSourcesList(mock_module)
        
        assert usl.module == mock_module
        assert usl.add_ppa_signing_keys_callback is None
        assert usl.codename == 'bionic'
    
    @patch('ansible.modules.apt_repository.distro')
    @patch('ansible.modules.apt_repository.apt_pkg')
    def test_init_with_add_ppa_signing_keys_callback(self, mock_apt_pkg, mock_distro):
        mock_module = Mock()
        mock_module.params = {'codename': 'focal'}
        mock_distro.codename = 'bionic'
        mock_callback = Mock()
        mock_apt_pkg.config = Mock()
        mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
        
        usl = UbuntuSourcesList(mock_module, add_ppa_signing_keys_callback=mock_callback)
        
        assert usl.module == mock_module
        assert usl.add_ppa_signing_keys_callback == mock_callback
        assert usl.codename == 'focal'
