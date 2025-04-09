# file: lib/ansible/modules/iptables.py:661-669
# asked: {"lines": [666, 668], "branches": [[665, 666], [667, 668]]}
# gained: {"lines": [666, 668], "branches": [[665, 666], [667, 668]]}

import pytest
from ansible.modules.iptables import push_arguments

def test_push_arguments_with_rule_num():
    iptables_path = "/sbin/iptables"
    action = "-I"
    params = {
        "table": "filter",
        "chain": "INPUT",
        "rule_num": "1",
        "protocol": "tcp",
        "source": "192.168.1.1",
        "destination": "192.168.1.2",
        "match": "tcp",
        "jump": "ACCEPT"
    }
    cmd = push_arguments(iptables_path, action, params, make_rule=False)
    assert cmd == [iptables_path, '-t', 'filter', '-I', 'INPUT', '1']

def test_push_arguments_with_make_rule(mocker):
    iptables_path = "/sbin/iptables"
    action = "-A"
    params = {
        "table": "filter",
        "chain": "INPUT",
        "protocol": "tcp",
        "source": "192.168.1.1",
        "destination": "192.168.1.2",
        "match": "tcp",
        "jump": "ACCEPT"
    }
    mocker.patch('ansible.modules.iptables.construct_rule', return_value=['-p', 'tcp', '-s', '192.168.1.1', '-d', '192.168.1.2', '-m', 'tcp', '-j', 'ACCEPT'])
    cmd = push_arguments(iptables_path, action, params, make_rule=True)
    assert cmd == [iptables_path, '-t', 'filter', '-A', 'INPUT', '-p', 'tcp', '-s', '192.168.1.1', '-d', '192.168.1.2', '-m', 'tcp', '-j', 'ACCEPT']
