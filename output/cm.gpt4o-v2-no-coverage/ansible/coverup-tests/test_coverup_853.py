# file: lib/ansible/module_utils/yumdnf.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.yumdnf import YumDnf

class TestYumDnf(YumDnf):
    def is_lockfile_pid_valid(self):
        return True

    def run(self):
        pass

@pytest.fixture
def module_params():
    return {
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
        'list': False,
        'name': ['package1', 'package2'],
        'releasever': None,
        'security': False,
        'skip_broken': False,
        'state': None,
        'update_only': False,
        'update_cache': False,
        'validate_certs': True,
        'lock_timeout': 30
    }

@pytest.fixture
def module(module_params):
    module = Mock()
    module.params = module_params
    return module

def test_yumdnf_init(module):
    yumdnf = TestYumDnf(module)
    assert yumdnf.module == module
    assert yumdnf.allow_downgrade == module.params['allow_downgrade']
    assert yumdnf.autoremove == module.params['autoremove']
    assert yumdnf.bugfix == module.params['bugfix']
    assert yumdnf.cacheonly == module.params['cacheonly']
    assert yumdnf.conf_file == module.params['conf_file']
    assert yumdnf.disable_excludes == module.params['disable_excludes']
    assert yumdnf.disable_gpg_check == module.params['disable_gpg_check']
    assert yumdnf.disable_plugin == module.params['disable_plugin']
    assert yumdnf.disablerepo == module.params['disablerepo']
    assert yumdnf.download_only == module.params['download_only']
    assert yumdnf.download_dir == module.params['download_dir']
    assert yumdnf.enable_plugin == module.params['enable_plugin']
    assert yumdnf.enablerepo == module.params['enablerepo']
    assert yumdnf.exclude == module.params['exclude']
    assert yumdnf.installroot == module.params['installroot']
    assert yumdnf.install_repoquery == module.params['install_repoquery']
    assert yumdnf.install_weak_deps == module.params['install_weak_deps']
    assert yumdnf.list == module.params['list']
    assert yumdnf.names == ['package1', 'package2']
    assert yumdnf.releasever == module.params['releasever']
    assert yumdnf.security == module.params['security']
    assert yumdnf.skip_broken == module.params['skip_broken']
    assert yumdnf.state == 'present'
    assert yumdnf.update_only == module.params['update_only']
    assert yumdnf.update_cache == module.params['update_cache']
    assert yumdnf.validate_certs == module.params['validate_certs']
    assert yumdnf.lock_timeout == module.params['lock_timeout']
    assert yumdnf.lockfile == '/var/run/yum.pid'

def test_yumdnf_autoremove_state_absent(module_params, module):
    module_params['autoremove'] = True
    module_params['state'] = None
    yumdnf = TestYumDnf(module)
    assert yumdnf.state == 'absent'

def test_yumdnf_autoremove_invalid_state(module_params, module):
    module_params['autoremove'] = True
    module_params['state'] = 'present'
    module.fail_json.side_effect = AssertionError("Autoremove should be used alone or with state=absent")
    with pytest.raises(AssertionError, match="Autoremove should be used alone or with state=absent"):
        TestYumDnf(module)

def test_yumdnf_invalid_package_name(module_params, module):
    module_params['name'] = ['invalid package']
    module.fail_json.side_effect = AssertionError("It appears that a space separated string of packages was passed in as an argument.")
    with pytest.raises(AssertionError, match="It appears that a space separated string of packages was passed in as an argument."):
        TestYumDnf(module)
