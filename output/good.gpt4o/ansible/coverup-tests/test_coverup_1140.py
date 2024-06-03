# file lib/ansible/executor/playbook_executor.py:321-336
# lines [327, 328, 329, 330, 331, 332, 333, 334, 336]
# branches ['330->331', '330->336']

import os
import pytest
from unittest import mock
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def playbook_executor():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return PlaybookExecutor(playbooks=[], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})

def test_generate_retry_inventory_success(playbook_executor, tmp_path):
    retry_path = tmp_path / "retry_file"
    replay_hosts = ["host1", "host2", "host3"]

    result = playbook_executor._generate_retry_inventory(str(retry_path), replay_hosts)

    assert result is True
    assert retry_path.exists()
    with open(retry_path, 'r') as f:
        lines = f.readlines()
        assert lines == ["host1\n", "host2\n", "host3\n"]

def test_generate_retry_inventory_failure(playbook_executor, mocker):
    retry_path = "/invalid_path/retry_file"
    replay_hosts = ["host1", "host2", "host3"]

    mocker.patch("ansible.executor.playbook_executor.makedirs_safe", side_effect=Exception("mocked exception"))
    mock_display_warning = mocker.patch("ansible.executor.playbook_executor.display.warning")

    result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)

    assert result is False
    mock_display_warning.assert_called_once_with("Could not create retry file '%s'.\n\t%s" % (retry_path, "mocked exception"))
