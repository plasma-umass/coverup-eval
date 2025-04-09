# file: lib/ansible/plugins/callback/default.py:317-322
# asked: {"lines": [318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [318, 319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_include_with_label(callback_module, monkeypatch):
    included_file = Mock()
    included_file._filename = 'test_file.yml'
    included_file._hosts = [Mock(), Mock()]
    included_file._hosts[0].name = 'host1'
    included_file._hosts[1].name = 'host2'
    included_file._vars = {'_ansible_item_label': 'test_label'}

    display_mock = Mock()
    monkeypatch.setattr(callback_module, '_display', display_mock)

    callback_module.v2_playbook_on_include(included_file)

    expected_msg = 'included: test_file.yml for host1, host2 => (item=test_label)'
    display_mock.display.assert_called_once_with(expected_msg, color=C.COLOR_SKIP)

def test_v2_playbook_on_include_without_label(callback_module, monkeypatch):
    included_file = Mock()
    included_file._filename = 'test_file.yml'
    included_file._hosts = [Mock(), Mock()]
    included_file._hosts[0].name = 'host1'
    included_file._hosts[1].name = 'host2'
    included_file._vars = {}

    display_mock = Mock()
    monkeypatch.setattr(callback_module, '_display', display_mock)

    callback_module.v2_playbook_on_include(included_file)

    expected_msg = 'included: test_file.yml for host1, host2'
    display_mock.display.assert_called_once_with(expected_msg, color=C.COLOR_SKIP)
