# file: lib/ansible/modules/iptables.py:661-669
# asked: {"lines": [661, 662, 663, 664, 665, 666, 667, 668, 669], "branches": [[665, 666], [665, 667], [667, 668], [667, 669]]}
# gained: {"lines": [661, 662, 663, 664, 665, 666, 667, 668, 669], "branches": [[665, 666], [665, 667], [667, 668], [667, 669]]}

import pytest

def test_push_arguments_insert_with_rule_num(monkeypatch):
    def mock_construct_rule(params):
        return ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    
    monkeypatch.setattr('ansible.modules.iptables.construct_rule', mock_construct_rule)
    
    from ansible.modules.iptables import push_arguments
    
    iptables_path = '/sbin/iptables'
    action = '-I'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': '1',
        'protocol': 'tcp',
        'source': None,
        'destination': None,
        'match': None,
        'tcp_flags': None,
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': None,
        'log_level': None,
        'to_destination': None,
        'destination_ports': None,
        'to_source': None,
        'goto': None,
        'in_interface': None,
        'out_interface': None,
        'fragment': None,
        'set_counters': None,
        'source_port': None,
        'destination_port': None,
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'syn': None,
        'ctstate': None,
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'comment': None,
        'ip_version': '4',
        'wait': None
    }
    
    result = push_arguments(iptables_path, action, params, make_rule=True)
    expected = [
        '/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '1',
        '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT'
    ]
    assert result == expected

def test_push_arguments_no_rule_num(monkeypatch):
    def mock_construct_rule(params):
        return ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    
    monkeypatch.setattr('ansible.modules.iptables.construct_rule', mock_construct_rule)
    
    from ansible.modules.iptables import push_arguments
    
    iptables_path = '/sbin/iptables'
    action = '-A'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'source': None,
        'destination': None,
        'match': None,
        'tcp_flags': None,
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': None,
        'log_level': None,
        'to_destination': None,
        'destination_ports': None,
        'to_source': None,
        'goto': None,
        'in_interface': None,
        'out_interface': None,
        'fragment': None,
        'set_counters': None,
        'source_port': None,
        'destination_port': None,
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'syn': None,
        'ctstate': None,
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'comment': None,
        'ip_version': '4',
        'wait': None
    }
    
    result = push_arguments(iptables_path, action, params, make_rule=True)
    expected = [
        '/sbin/iptables', '-t', 'filter', '-A', 'INPUT',
        '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT'
    ]
    assert result == expected

def test_push_arguments_no_make_rule():
    from ansible.modules.iptables import push_arguments
    
    iptables_path = '/sbin/iptables'
    action = '-A'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'source': None,
        'destination': None,
        'match': None,
        'tcp_flags': None,
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': None,
        'log_level': None,
        'to_destination': None,
        'destination_ports': None,
        'to_source': None,
        'goto': None,
        'in_interface': None,
        'out_interface': None,
        'fragment': None,
        'set_counters': None,
        'source_port': None,
        'destination_port': None,
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'syn': None,
        'ctstate': None,
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'comment': None,
        'ip_version': '4',
        'wait': None
    }
    
    result = push_arguments(iptables_path, action, params, make_rule=False)
    expected = [
        '/sbin/iptables', '-t', 'filter', '-A', 'INPUT'
    ]
    assert result == expected
