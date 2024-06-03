# file lib/ansible/plugins/callback/junit.py:310-311
# lines [310, 311]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_stats(callback_module, mocker):
    mock_generate_report = mocker.patch.object(callback_module, '_generate_report')
    stats = MagicMock()
    
    callback_module.v2_playbook_on_stats(stats)
    
    mock_generate_report.assert_called_once()
