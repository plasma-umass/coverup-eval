# file lib/ansible/executor/playbook_executor.py:321-336
# lines [327, 328, 329, 330, 331, 332, 333, 334, 336]
# branches ['330->331', '330->336']

import os
import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'warning')

# Test function to cover lines 327-336
def test_generate_retry_inventory_exception_handling(tmp_path, mock_display):
    with patch('ansible.executor.playbook_executor.PlaybookExecutor.__init__', return_value=None):
        with patch('ansible.executor.playbook_executor.makedirs_safe') as mock_makedirs_safe:
            mock_makedirs_safe.side_effect = Exception("Mocked exception")
            executor = PlaybookExecutor()
            retry_path = str(tmp_path / "retry_file.retry")
            replay_hosts = ['host1', 'host2']

            # Run the method that should now raise an exception and return False
            result = executor._generate_retry_inventory(retry_path, replay_hosts)

            # Assert that the result is False due to the exception
            assert result is False
