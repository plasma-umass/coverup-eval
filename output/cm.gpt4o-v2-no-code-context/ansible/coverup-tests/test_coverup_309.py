# file: lib/ansible/modules/iptables.py:661-669
# asked: {"lines": [661, 662, 663, 664, 665, 666, 667, 668, 669], "branches": [[665, 666], [665, 667], [667, 668], [667, 669]]}
# gained: {"lines": [661, 662, 663, 664, 665, 666, 667, 668, 669], "branches": [[665, 666], [665, 667], [667, 668], [667, 669]]}

import pytest

# Mock function to replace construct_rule
def mock_construct_rule(params):
    return ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']

def test_push_arguments_insert_with_rule_num(monkeypatch):
    from ansible.modules.iptables import push_arguments

    # Mocking construct_rule function
    monkeypatch.setattr('ansible.modules.iptables.construct_rule', mock_construct_rule)

    iptables_path = '/sbin/iptables'
    action = '-I'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': '1',
        'protocol': 'tcp',
        'dport': '80',
        'target': 'ACCEPT'
    }

    result = push_arguments(iptables_path, action, params)
    expected = ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '1', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    assert result == expected

def test_push_arguments_insert_without_rule_num(monkeypatch):
    from ansible.modules.iptables import push_arguments

    # Mocking construct_rule function
    monkeypatch.setattr('ansible.modules.iptables.construct_rule', mock_construct_rule)

    iptables_path = '/sbin/iptables'
    action = '-I'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'dport': '80',
        'target': 'ACCEPT'
    }

    result = push_arguments(iptables_path, action, params)
    expected = ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    assert result == expected

def test_push_arguments_no_make_rule(monkeypatch):
    from ansible.modules.iptables import push_arguments

    # Mocking construct_rule function
    monkeypatch.setattr('ansible.modules.iptables.construct_rule', mock_construct_rule)

    iptables_path = '/sbin/iptables'
    action = '-A'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'dport': '80',
        'target': 'ACCEPT'
    }

    result = push_arguments(iptables_path, action, params, make_rule=False)
    expected = ['/sbin/iptables', '-t', 'filter', '-A', 'INPUT']
    assert result == expected
