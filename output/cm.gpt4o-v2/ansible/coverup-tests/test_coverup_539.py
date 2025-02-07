# file: lib/ansible/plugins/callback/default.py:317-322
# asked: {"lines": [317, 318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [317, 318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def included_file():
    included_file = MagicMock()
    included_file._filename = 'test_file.yml'
    host1 = MagicMock()
    host1.name = 'host1'
    host2 = MagicMock()
    host2.name = 'host2'
    included_file._hosts = [host1, host2]
    included_file._vars = {'ansible_loop_var': 'item', 'item': 'test_item'}
    return included_file

def test_v2_playbook_on_include_with_label(included_file):
    callback = CallbackModule()
    callback._display = MagicMock()
    
    with patch.object(callback, '_get_item_label', return_value='test_item'):
        callback.v2_playbook_on_include(included_file)
    
    expected_msg = 'included: test_file.yml for host1, host2 => (item=test_item)'
    callback._display.display.assert_called_once_with(expected_msg, color=C.COLOR_SKIP)

def test_v2_playbook_on_include_without_label(included_file):
    callback = CallbackModule()
    callback._display = MagicMock()
    
    with patch.object(callback, '_get_item_label', return_value=None):
        callback.v2_playbook_on_include(included_file)
    
    expected_msg = 'included: test_file.yml for host1, host2'
    callback._display.display.assert_called_once_with(expected_msg, color=C.COLOR_SKIP)
