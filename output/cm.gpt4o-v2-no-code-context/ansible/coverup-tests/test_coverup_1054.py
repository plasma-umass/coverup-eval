# file: lib/ansible/modules/apt_repository.py:422-426
# asked: {"lines": [423, 424, 425, 426], "branches": []}
# gained: {"lines": [423, 424, 425, 426], "branches": []}

import pytest
from unittest import mock

# Assuming the UbuntuSourcesList and SourcesList classes are imported from ansible/modules/apt_repository.py

class TestUbuntuSourcesList:
    @pytest.fixture
    def mock_module(self):
        module = mock.Mock()
        module.params = {'codename': 'focal'}
        return module

    @pytest.fixture
    def mock_distro(self, monkeypatch):
        distro = mock.Mock()
        distro.codename = 'bionic'
        monkeypatch.setattr('ansible.modules.apt_repository.distro', distro)
        return distro

    @pytest.fixture
    def mock_apt_pkg(self, monkeypatch):
        apt_pkg = mock.Mock()
        apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
        monkeypatch.setattr('ansible.modules.apt_repository.apt_pkg', apt_pkg)
        return apt_pkg

    def test_ubuntu_sources_list_init_with_codename(self, mock_module, mock_apt_pkg):
        from ansible.modules.apt_repository import UbuntuSourcesList

        # Test with codename in module params
        obj = UbuntuSourcesList(mock_module)
        assert obj.module == mock_module
        assert obj.add_ppa_signing_keys_callback is None
        assert obj.codename == 'focal'

    def test_ubuntu_sources_list_init_without_codename(self, mock_module, mock_distro, mock_apt_pkg):
        from ansible.modules.apt_repository import UbuntuSourcesList

        # Test without codename in module params
        mock_module.params['codename'] = None
        obj = UbuntuSourcesList(mock_module)
        assert obj.module == mock_module
        assert obj.add_ppa_signing_keys_callback is None
        assert obj.codename == 'bionic'
