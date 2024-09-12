# file: lib/ansible/modules/dnf.py:773-791
# asked: {"lines": [773, 774, 776, 777, 778, 779, 781, 782, 783, 784, 786, 788, 789, 791], "branches": [[778, 779], [778, 781], [782, 783], [782, 786], [788, 789], [788, 791]]}
# gained: {"lines": [773, 774, 776, 777, 778, 779, 781, 782, 783, 784, 786, 788, 789, 791], "branches": [[778, 779], [778, 781], [782, 783], [782, 786], [788, 789], [788, 791]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.yumdnf import YumDnf
from ansible.modules.dnf import DnfModule

@pytest.fixture
def dnf_module():
    module = MagicMock()
    module.params = {
        'allowerasing': False,
        'nobest': False,
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
        'name': [],
        'releasever': None,
        'security': False,
        'skip_broken': False,
        'state': 'present',
        'update_only': False,
        'update_cache': False,
        'validate_certs': True,
        'lock_timeout': 30,
    }
    with patch('ansible.modules.dnf.get_best_parsable_locale', return_value='C'):
        dnf_module = DnfModule(module)
        dnf_module.base = MagicMock()  # Mock the base attribute
        return dnf_module

def test_is_installed_with_arch(dnf_module, mocker):
    mocker.patch.object(dnf_module, '_split_package_arch', return_value=('pkgname', 'x86_64'))
    mocker.patch.object(dnf_module, '_packagename_dict', return_value={'name': 'pkgname', 'epoch': '0', 'version': '1.0', 'release': '1'})
    mock_query = mocker.MagicMock()
    mock_query.installed.return_value.filter.return_value = True
    dnf_module.base.sack.query.return_value = mock_query

    assert dnf_module._is_installed('pkgname.x86_64') is True

def test_is_installed_without_arch(dnf_module, mocker):
    mocker.patch.object(dnf_module, '_split_package_arch', return_value=('pkgname', None))
    mocker.patch.object(dnf_module, '_packagename_dict', return_value={'name': 'pkgname', 'epoch': '0', 'version': '1.0', 'release': '1'})
    mock_query = mocker.MagicMock()
    mock_query.installed.return_value.filter.return_value = True
    dnf_module.base.sack.query.return_value = mock_query

    assert dnf_module._is_installed('pkgname') is True

def test_is_installed_no_package_details(dnf_module, mocker):
    mocker.patch.object(dnf_module, '_split_package_arch', return_value=('pkgname', None))
    mocker.patch.object(dnf_module, '_packagename_dict', return_value=None)
    mock_query = mocker.MagicMock()
    mock_query.installed.return_value.filter.return_value = True
    dnf_module.base.sack.query.return_value = mock_query

    assert dnf_module._is_installed('pkgname') is True

def test_is_not_installed(dnf_module, mocker):
    mocker.patch.object(dnf_module, '_split_package_arch', return_value=('pkgname', None))
    mocker.patch.object(dnf_module, '_packagename_dict', return_value={'name': 'pkgname', 'epoch': '0', 'version': '1.0', 'release': '1'})
    mock_query = mocker.MagicMock()
    mock_query.installed.return_value.filter.return_value = False
    dnf_module.base.sack.query.return_value = mock_query

    assert dnf_module._is_installed('pkgname') is False
