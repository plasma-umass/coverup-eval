# file lib/ansible/modules/apt_repository.py:443-452
# lines [443, 444, 445, 446, 447, 448, 449, 451, 452]
# branches []

import pytest
from unittest import mock

# Assuming the class UbuntuSourcesList is defined in ansible.modules.apt_repository
from ansible.modules.apt_repository import UbuntuSourcesList

class TestUbuntuSourcesList:
    @pytest.fixture
    def ubuntu_sources_list(self):
        module_mock = mock.Mock()
        module_mock.params = {'codename': 'focal'}
        with mock.patch('ansible.modules.apt_repository.SourcesList.__init__', return_value=None):
            return UbuntuSourcesList(module=module_mock)

    def test_expand_ppa_with_full_path(self, ubuntu_sources_list):
        line, ppa_owner, ppa_name = ubuntu_sources_list._expand_ppa('ppa:owner/name')
        assert line == 'deb http://ppa.launchpad.net/owner/name/ubuntu focal main'
        assert ppa_owner == 'owner'
        assert ppa_name == 'name'

    def test_expand_ppa_with_default_name(self, ubuntu_sources_list):
        line, ppa_owner, ppa_name = ubuntu_sources_list._expand_ppa('ppa:owner')
        assert line == 'deb http://ppa.launchpad.net/owner/ppa/ubuntu focal main'
        assert ppa_owner == 'owner'
        assert ppa_name == 'ppa'
