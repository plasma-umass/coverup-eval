# file: lib/ansible/plugins/callback/default.py:317-322
# asked: {"lines": [317, 318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [317, 318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_include_no_label(callback_module, mocker):
    included_file = Mock()
    included_file._filename = 'test_file.yml'
    included_file._hosts = [Mock(), Mock()]
    included_file._hosts[0].name = 'host1'
    included_file._hosts[1].name = 'host2'
    included_file._vars = {}

    mock_display = mocker.patch.object(callback_module._display, 'display')

    mocker.patch.object(callback_module, '_get_item_label', return_value=None)

    callback_module.v2_playbook_on_include(included_file)

    expected_msg = 'included: test_file.yml for host1, host2'
    mock_display.assert_called_once_with(expected_msg, color='cyan')

def test_v2_playbook_on_include_with_label(callback_module, mocker):
    included_file = Mock()
    included_file._filename = 'test_file.yml'
    included_file._hosts = [Mock(), Mock()]
    included_file._hosts[0].name = 'host1'
    included_file._hosts[1].name = 'host2'
    included_file._vars = {}

    mock_display = mocker.patch.object(callback_module._display, 'display')

    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')

    callback_module.v2_playbook_on_include(included_file)

    expected_msg = 'included: test_file.yml for host1, host2 => (item=item_label)'
    mock_display.assert_called_once_with(expected_msg, color='cyan')
