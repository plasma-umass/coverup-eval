# file: lib/ansible/modules/debconf.py:129-142
# asked: {"lines": [130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142], "branches": [[132, 133], [132, 135], [135, 136], [135, 140], [136, 137], [136, 138], [138, 139], [138, 140]]}
# gained: {"lines": [130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142], "branches": [[132, 133], [132, 135], [135, 136], [135, 140], [136, 137], [136, 138], [138, 139]]}

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule

# Mocking the AnsibleModule to avoid actual system calls
@pytest.fixture
def module():
    return mock.Mock(spec=AnsibleModule)

def test_set_selection_with_unseen_true(module):
    from ansible.modules.debconf import set_selection

    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    pkg = 'testpkg'
    question = 'test/question'
    vtype = 'string'
    value = 'testvalue'
    unseen = True

    result = set_selection(module, pkg, question, vtype, value, unseen)

    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections', '-u'], data='testpkg test/question string testvalue')
    assert result == (0, '', '')

def test_set_selection_with_boolean_true(module):
    from ansible.modules.debconf import set_selection

    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    pkg = 'testpkg'
    question = 'test/question'
    vtype = 'boolean'
    value = 'True'
    unseen = False

    result = set_selection(module, pkg, question, vtype, value, unseen)

    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='testpkg test/question boolean true')
    assert result == (0, '', '')

def test_set_selection_with_boolean_false(module):
    from ansible.modules.debconf import set_selection

    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    pkg = 'testpkg'
    question = 'test/question'
    vtype = 'boolean'
    value = 'False'
    unseen = False

    result = set_selection(module, pkg, question, vtype, value, unseen)

    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='testpkg test/question boolean false')
    assert result == (0, '', '')
