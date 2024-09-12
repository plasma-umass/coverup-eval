# file: lib/ansible/modules/iptables.py:704-711
# asked: {"lines": [704, 705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}
# gained: {"lines": [704, 705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}

import pytest
import re
from unittest.mock import Mock

# Assuming push_arguments is defined elsewhere and imported
from ansible.modules.iptables import get_chain_policy, push_arguments

@pytest.fixture
def mock_module():
    return Mock()

def test_get_chain_policy_with_policy(mock_module, monkeypatch):
    iptables_path = '/sbin/iptables'
    params = ['INPUT']
    
    def mock_run_command(cmd, check_rc):
        return (0, "Chain INPUT (policy ACCEPT)", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', lambda *args, **kwargs: 'mocked_cmd')
    
    result = get_chain_policy(iptables_path, mock_module, params)
    assert result == 'ACCEPT'

def test_get_chain_policy_without_policy(mock_module, monkeypatch):
    iptables_path = '/sbin/iptables'
    params = ['INPUT']
    
    def mock_run_command(cmd, check_rc):
        return (0, "Chain INPUT (policy NONE)", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', lambda *args, **kwargs: 'mocked_cmd')
    
    result = get_chain_policy(iptables_path, mock_module, params)
    assert result == 'NONE'

def test_get_chain_policy_no_policy_in_output(mock_module, monkeypatch):
    iptables_path = '/sbin/iptables'
    params = ['INPUT']
    
    def mock_run_command(cmd, check_rc):
        return (0, "Chain INPUT", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', lambda *args, **kwargs: 'mocked_cmd')
    
    result = get_chain_policy(iptables_path, mock_module, params)
    assert result is None
