# file lib/ansible/module_utils/facts/system/dns.py:25-67
# lines [40, 63]
# branches ['39->40', '47->35', '57->35', '59->35', '62->63']

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.dns import DnsFactCollector

@pytest.fixture
def dns_fact_collector():
    return DnsFactCollector()

def test_collect_empty_lines(dns_fact_collector):
    mock_content = "\n\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {}}

def test_collect_comment_lines(dns_fact_collector):
    mock_content = "# This is a comment\n; Another comment\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {}}

def test_collect_nameserver(dns_fact_collector):
    mock_content = "nameserver 8.8.8.8\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'nameservers': ['8.8.8.8']}}

def test_collect_domain(dns_fact_collector):
    mock_content = "domain example.com\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'domain': 'example.com'}}

def test_collect_search(dns_fact_collector):
    mock_content = "search example.com sub.example.com\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'search': ['example.com', 'sub.example.com']}}

def test_collect_sortlist(dns_fact_collector):
    mock_content = "sortlist 192.168.1.0/255.255.255.0\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'sortlist': ['192.168.1.0/255.255.255.0']}}

def test_collect_options(dns_fact_collector):
    mock_content = "options timeout:2 attempts:3\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'options': {'timeout': '2', 'attempts': '3'}}}

def test_collect_options_empty(dns_fact_collector):
    mock_content = "options\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'options': {}}}

def test_collect_options_invalid(dns_fact_collector):
    mock_content = "options invalid_option\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=mock_content):
        result = dns_fact_collector.collect()
        assert result == {'dns': {'options': {'invalid_option': True}}}
