# file lib/ansible/module_utils/facts/network/linux.py:47-62
# lines [51]
# branches ['50->51']

import pytest
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path = mocker.MagicMock(return_value=None)
    return mock_module

def test_linux_network_populate_without_ip(mock_module):
    linux_network = LinuxNetwork(module=mock_module)
    facts = linux_network.populate()
    assert isinstance(facts, dict)
    assert len(facts) == 0
