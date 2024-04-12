# file lib/ansible/modules/dnf.py:432-456
# lines [436, 437, 438, 439, 440, 441, 442, 445, 449, 451, 452, 454, 456]
# branches ['451->452', '451->454']

import pytest
from unittest.mock import MagicMock

# Assuming the DnfModule class is part of the module ansible.modules.dnf
from ansible.modules.dnf import DnfModule

@pytest.fixture
def dnf_module(mocker):
    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, 'en_US.UTF-8\nC.UTF-8\n', '')
    mocker.patch('ansible.modules.dnf.YumDnf', autospec=True)
    return DnfModule(module_mock)

@pytest.fixture
def package_mock(mocker):
    package = MagicMock()
    package.name = 'testpkg'
    package.arch = 'noarch'
    package.epoch = '0'
    package.release = '1'
    package.version = '1.0.0'
    package.repoid = 'testrepo'
    return package

def test_package_dict_available(dnf_module, package_mock):
    package_mock.installtime = 0
    result = dnf_module._package_dict(package_mock)
    assert result['name'] == 'testpkg'
    assert result['arch'] == 'noarch'
    assert result['epoch'] == '0'
    assert result['release'] == '1'
    assert result['version'] == '1.0.0'
    assert result['repo'] == 'testrepo'
    assert result['envra'] == '0:testpkg-1.0.0-1.noarch'
    assert result['nevra'] == '0:testpkg-1.0.0-1.noarch'
    assert result['yumstate'] == 'available'

def test_package_dict_installed(dnf_module, package_mock):
    package_mock.installtime = 123456789
    result = dnf_module._package_dict(package_mock)
    assert result['name'] == 'testpkg'
    assert result['arch'] == 'noarch'
    assert result['epoch'] == '0'
    assert result['release'] == '1'
    assert result['version'] == '1.0.0'
    assert result['repo'] == 'testrepo'
    assert result['envra'] == '0:testpkg-1.0.0-1.noarch'
    assert result['nevra'] == '0:testpkg-1.0.0-1.noarch'
    assert result['yumstate'] == 'installed'
