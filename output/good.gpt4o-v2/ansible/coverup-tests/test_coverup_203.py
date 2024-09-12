# file: lib/ansible/plugins/callback/junit.py:255-274
# asked: {"lines": [255, 258, 260, 261, 262, 264, 265, 267, 268, 269, 271, 273, 274], "branches": [[260, 261], [260, 267], [261, 262], [261, 264], [264, 260], [264, 265]]}
# gained: {"lines": [255, 258, 260, 261, 262, 264, 265, 267, 268, 269, 271, 273, 274], "branches": [[260, 261], [260, 267], [261, 262], [261, 264], [264, 260], [264, 265]]}

import os
import time
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.plugins.callback.junit import CallbackModule
from ansible.utils._junit_xml import TestSuite, TestSuites, TestCase

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._task_data = {
        'task1': MagicMock(action='setup', host_data={'host1': MagicMock()}),
        'task2': MagicMock(action='action2', host_data={'host2': MagicMock()})
    }
    cb._include_setup_tasks_in_report = 'false'
    cb._playbook_name = 'test_playbook'
    cb._output_dir = '/tmp'
    cb._build_test_case = MagicMock(return_value=TestCase(name='test_case'))
    return cb

def test_generate_report(callback_module, monkeypatch):
    mock_time = 1234567890
    mock_file = mock_open()
    monkeypatch.setattr(time, 'time', lambda: mock_time)
    monkeypatch.setattr('builtins.open', mock_file)
    monkeypatch.setattr(os.path, 'join', lambda *args: '/tmp/test_playbook-1234567890.xml')

    callback_module._generate_report()

    expected_report = TestSuites(suites=[TestSuite(name='test_playbook', cases=[TestCase(name='test_case')])]).to_pretty_xml()
    mock_file.assert_called_once_with('/tmp/test_playbook-1234567890.xml', 'wb')
    mock_file().write.assert_called_once_with(expected_report.encode('utf-8', errors='surrogate_or_strict'))
