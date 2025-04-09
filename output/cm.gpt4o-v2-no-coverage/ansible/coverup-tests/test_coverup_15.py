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
        'allow_downgrade': True,
        'autoremove': False,
        'bugfix': False,
        'cacheonly': False,
        'conf_file': '/etc/yum.conf',
        'disable_excludes': None,
        'disable_gpg_check': False,
        'disable_plugin': False,
        'disablerepo': ['repo1,repo2'],
        'download_only': False,
        'download_dir': '/tmp',
        'enable_plugin': False,
        'enablerepo': ['repo3,repo4'],
        'exclude': ['pkg1,pkg2'],
        'installroot': '/',
        'install_repoquery': False,
        'install_weak_deps': False,
        'list': None,
        'name': ['pkg3, pkg4'],
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
    
    assert yumdnf.allow_downgrade == True
    assert yumdnf.autoremove == False
    assert yumdnf.bugfix == False
    assert yumdnf.cacheonly == False
    assert yumdnf.conf_file == '/etc/yum.conf'
    assert yumdnf.disable_excludes == None
    assert yumdnf.disable_gpg_check == False
    assert yumdnf.disable_plugin == False
    assert yumdnf.disablerepo == ['repo1', 'repo2']
    assert yumdnf.download_only == False
    assert yumdnf.download_dir == '/tmp'
    assert yumdnf.enable_plugin == False
    assert yumdnf.enablerepo == ['repo3', 'repo4']
    assert yumdnf.exclude == ['pkg1', 'pkg2']
    assert yumdnf.installroot == '/'
    assert yumdnf.install_repoquery == False
    assert yumdnf.install_weak_deps == False
    assert yumdnf.list == None
    assert yumdnf.names == ['pkg3', 'pkg4']
    assert yumdnf.releasever == None
    assert yumdnf.security == False
    assert yumdnf.skip_broken == False
    assert yumdnf.state == 'present'
    assert yumdnf.update_only == False
    assert yumdnf.update_cache == False
    assert yumdnf.validate_certs == True
    assert yumdnf.lock_timeout == 30
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
        results=[],
    )

def test_yumdnf_space_separated_names(module):
    module.params['name'] = ['pkg1 pkg2']
    with pytest.raises(Exception, match="fail_json called"):
        YumDnfConcrete(module)
    module.fail_json.assert_called_once_with(
        msg='It appears that a space separated string of packages was passed in as an argument. To operate on several packages, pass a comma separated string of packages or a list of packages.'
    )
