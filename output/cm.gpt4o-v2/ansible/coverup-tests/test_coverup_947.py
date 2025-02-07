# file: lib/ansible/plugins/callback/junit.py:310-311
# asked: {"lines": [310, 311], "branches": []}
# gained: {"lines": [310, 311], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._generate_report = MagicMock()
    return module

def test_v2_playbook_on_stats(callback_module):
    stats = MagicMock()
    callback_module.v2_playbook_on_stats(stats)
    callback_module._generate_report.assert_called_once()
