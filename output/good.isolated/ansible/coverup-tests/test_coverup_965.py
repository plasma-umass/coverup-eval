# file lib/ansible/plugins/callback/junit.py:310-311
# lines [310, 311]
# branches []

# test_junit.py
import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def junit_callback():
    return CallbackModule()

def test_v2_playbook_on_stats(junit_callback):
    stats = MagicMock()
    with patch.object(CallbackModule, '_generate_report') as mock_generate_report:
        junit_callback.v2_playbook_on_stats(stats)
        mock_generate_report.assert_called_once()

# Ensure that the test cleans up after itself
def teardown_module(module):
    # Clean up any state here if necessary
    pass
