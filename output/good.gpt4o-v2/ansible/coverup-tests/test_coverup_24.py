# file: lib/ansible/module_utils/yumdnf.py:68-132
# asked: {"lines": [68, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 102, 103, 104, 105, 109, 110, 111, 112, 118, 119, 120, 122, 124, 125, 126, 127, 132], "branches": [[109, 110], [109, 118], [110, 109], [110, 111], [118, 119], [118, 124], [119, 120], [119, 122], [124, 125], [124, 132]]}
# gained: {"lines": [68, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 102, 103, 104, 105, 109, 110, 111, 112, 118, 119, 120, 122, 124, 125, 126, 127, 132], "branches": [[109, 110], [109, 118], [110, 109], [110, 111], [118, 119], [118, 124], [119, 120], [119, 122], [124, 125], [124, 132]]}

import pytest
from unittest.mock import Mock

from ansible.module_utils.yumdnf import YumDnf

class YumDnfConcrete(YumDnf):
    def is_lockfile_pid_valid(self):
        return True

    def run(self):
        pass

@pytest.fixture
def module():
    params = {
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
        'name': ['package1', 'package2'],
        'releasever': None,
        'security': False,
        'skip_broken': False,
        'state': None,
        'update_only': False,
        'update_cache': False,
        'validate_certs': True,
        'lock_timeout': 30,
    }
    module = Mock()
    module.params = params
    module.fail_json = Mock(side_effect=Exception("fail_json called"))
    return module

def test_yumdnf_init(module):
    yumdnf = YumDnfConcrete(module)
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

def test_yumdnf_autoremove_state_absent(module):
    module.params['autoremove'] = True
    module.params['state'] = None
    yumdnf = YumDnfConcrete(module)
    assert yumdnf.state == 'absent'

def test_yumdnf_autoremove_fail(module):
    module.params['autoremove'] = True
    module.params['state'] = 'present'
    with pytest.raises(Exception, match="fail_json called"):
        YumDnfConcrete(module)
    module.fail_json.assert_called_once_with(
        msg="Autoremove should be used alone or with state=absent",
        results=[]
    )

def test_yumdnf_space_separated_string(module):
    module.params['name'] = ['package1 package2']
    with pytest.raises(Exception, match="fail_json called"):
        YumDnfConcrete(module)
    module.fail_json.assert_called_once_with(
        msg='It appears that a space separated string of packages was passed in as an argument. To operate on several packages, pass a comma separated string of packages or a list of packages.'
    )

def test_listify_comma_sep_strings_in_list(module):
    yumdnf = YumDnfConcrete(module)
    result = yumdnf.listify_comma_sep_strings_in_list(['pkg1,pkg2', 'pkg3'])
    assert sorted(result) == ['pkg1', 'pkg2', 'pkg3']
