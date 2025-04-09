# file: lib/ansible/modules/dnf.py:432-456
# asked: {"lines": [432, 436, 437, 438, 439, 440, 441, 442, 445, 449, 451, 452, 454, 456], "branches": [[451, 452], [451, 454]]}
# gained: {"lines": [432, 436, 437, 438, 439, 440, 441, 442, 445, 449, 451, 452, 454, 456], "branches": [[451, 452], [451, 454]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.yumdnf import YumDnf
from ansible.modules.dnf import DnfModule

class TestDnfModule:
    
    @pytest.fixture
    def package_mock(self):
        package = Mock()
        package.name = "test_package"
        package.arch = "x86_64"
        package.epoch = 0
        package.release = "1"
        package.version = "1.0.0"
        package.repoid = "base"
        package.installtime = 0
        return package

    @pytest.fixture
    def dnf_module(self):
        module = Mock()
        module.params = {
            'allow_downgrade': False,
            'autoremove': False,
            'bugfix': False,
            'cacheonly': False,
            'conf_file': None,
            'disable_excludes': None,
            'disable_gpg_check': False,
            'disable_plugin': False,
            'disablerepo': [],
            'download_only': False,
            'download_dir': None,
            'enable_plugin': False,
            'enablerepo': [],
            'exclude': [],
            'installroot': '/',
            'install_repoquery': False,
            'install_weak_deps': False,
            'list': None,
            'name': ['test_package'],
            'releasever': None,
            'security': False,
            'skip_broken': False,
            'state': 'present',
            'update_only': False,
            'update_cache': False,
            'validate_certs': True,
            'lock_timeout': 30,
            'allowerasing': False,
            'nobest': False
        }
        with patch('ansible.modules.dnf.get_best_parsable_locale', return_value='C'):
            with patch('ansible.modules.dnf.dnf', create=True):
                return DnfModule(module)

    def test_package_dict_available(self, dnf_module, package_mock):
        package_mock.installtime = 0
        result = dnf_module._package_dict(package_mock)
        assert result['name'] == "test_package"
        assert result['arch'] == "x86_64"
        assert result['epoch'] == "0"
        assert result['release'] == "1"
        assert result['version'] == "1.0.0"
        assert result['repo'] == "base"
        assert result['envra'] == "0:test_package-1.0.0-1.x86_64"
        assert result['nevra'] == "0:test_package-1.0.0-1.x86_64"
        assert result['yumstate'] == "available"

    def test_package_dict_installed(self, dnf_module, package_mock):
        package_mock.installtime = 123456789
        result = dnf_module._package_dict(package_mock)
        assert result['name'] == "test_package"
        assert result['arch'] == "x86_64"
        assert result['epoch'] == "0"
        assert result['release'] == "1"
        assert result['version'] == "1.0.0"
        assert result['repo'] == "base"
        assert result['envra'] == "0:test_package-1.0.0-1.x86_64"
        assert result['nevra'] == "0:test_package-1.0.0-1.x86_64"
        assert result['yumstate'] == "installed"
