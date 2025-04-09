# file: lib/ansible/module_utils/yumdnf.py:155-176
# asked: {"lines": [155, 161, 162, 163, 164, 165, 166, 168, 169, 171, 173, 174, 176], "branches": [[163, 164], [163, 168], [164, 163], [164, 165], [168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [155, 161, 162, 163, 164, 165, 166, 168, 169, 171, 173, 174, 176], "branches": [[163, 164], [163, 168], [164, 163], [164, 165], [168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.module_utils.yumdnf import YumDnf

class TestYumDnf(YumDnf):
    def is_lockfile_pid_valid(self):
        pass

    def run(self):
        pass

@pytest.fixture
def yumdnf_instance():
    module = type('obj', (object,), {'params': {
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
        'name': '',
        'releasever': None,
        'security': False,
        'skip_broken': False,
        'state': None,
        'update_only': False,
        'update_cache': False,
        'validate_certs': True,
        'lock_timeout': 30
    }})
    return TestYumDnf(module)

def test_listify_comma_sep_strings_in_list(yumdnf_instance):
    # Test case 1: List with comma-separated strings
    input_list = ['pkg1, pkg2', 'pkg3']
    expected_output = ['pkg3', 'pkg1', 'pkg2']
    assert yumdnf_instance.listify_comma_sep_strings_in_list(input_list) == expected_output

    # Test case 2: List with no comma-separated strings
    input_list = ['pkg1', 'pkg2', 'pkg3']
    expected_output = ['pkg1', 'pkg2', 'pkg3']
    assert yumdnf_instance.listify_comma_sep_strings_in_list(input_list) == expected_output

    # Test case 3: List with empty string
    input_list = ['']
    expected_output = []
    assert yumdnf_instance.listify_comma_sep_strings_in_list(input_list) == expected_output

    # Test case 4: List with mixed comma-separated and non-comma-separated strings
    input_list = ['pkg1, pkg2', 'pkg3', 'pkg4, pkg5']
    expected_output = ['pkg3', 'pkg1', 'pkg2', 'pkg4', 'pkg5']
    assert yumdnf_instance.listify_comma_sep_strings_in_list(input_list) == expected_output
