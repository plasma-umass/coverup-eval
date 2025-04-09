# file lib/ansible/modules/debconf.py:129-142
# lines [129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142]
# branches ['132->133', '132->135', '135->136', '135->140', '136->137', '136->138', '138->139', '138->140']

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule

def test_set_selection(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    from ansible.modules.debconf import set_selection

    # Test unseen flag
    result = set_selection(module, 'testpkg', 'testquestion', 'string', 'testvalue', unseen=True)
    assert result == (0, '', '')
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections', '-u'], data='testpkg testquestion string testvalue')

    # Reset mock
    module.run_command.reset_mock()

    # Test boolean value 'True'
    result = set_selection(module, 'testpkg', 'testquestion', 'boolean', 'True', unseen=False)
    assert result == (0, '', '')
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='testpkg testquestion boolean true')

    # Reset mock
    module.run_command.reset_mock()

    # Test boolean value 'False'
    result = set_selection(module, 'testpkg', 'testquestion', 'boolean', 'False', unseen=False)
    assert result == (0, '', '')
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='testpkg testquestion boolean false')

    # Reset mock
    module.run_command.reset_mock()

    # Test without unseen flag and non-boolean value
    result = set_selection(module, 'testpkg', 'testquestion', 'string', 'testvalue', unseen=False)
    assert result == (0, '', '')
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='testpkg testquestion string testvalue')
