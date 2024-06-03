# file lib/ansible/module_utils/facts/system/dns.py:25-67
# lines [25, 26, 27, 29, 30, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67]
# branches ['35->36', '35->67', '36->37', '36->38', '39->40', '39->41', '41->42', '41->46', '42->43', '42->44', '44->35', '44->45', '46->47', '46->49', '47->35', '47->48', '49->50', '49->53', '51->35', '51->52', '53->54', '53->57', '55->35', '55->56', '57->35', '57->58', '59->35', '59->60', '60->35', '60->61', '62->63', '62->64']

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.dns import DnsFactCollector

@pytest.fixture
def dns_fact_collector():
    return DnsFactCollector()

def test_collect_nameservers(dns_fact_collector):
    resolv_conf_content = "nameserver 8.8.8.8\nnameserver 8.8.4.4\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']

def test_collect_domain(dns_fact_collector):
    resolv_conf_content = "domain example.com\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert 'domain' in facts['dns']
        assert facts['dns']['domain'] == 'example.com'

def test_collect_search(dns_fact_collector):
    resolv_conf_content = "search example.com sub.example.com\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert 'search' in facts['dns']
        assert facts['dns']['search'] == ['example.com', 'sub.example.com']

def test_collect_sortlist(dns_fact_collector):
    resolv_conf_content = "sortlist 192.168.1.0/255.255.255.0\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert 'sortlist' in facts['dns']
        assert facts['dns']['sortlist'] == ['192.168.1.0/255.255.255.0']

def test_collect_options(dns_fact_collector):
    resolv_conf_content = "options timeout:2 attempts:3\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert 'options' in facts['dns']
        assert facts['dns']['options'] == {'timeout': '2', 'attempts': '3'}

def test_collect_empty_lines_and_comments(dns_fact_collector):
    resolv_conf_content = "\n# This is a comment\n; Another comment\n"
    with patch('ansible.module_utils.facts.system.dns.get_file_content', return_value=resolv_conf_content):
        facts = dns_fact_collector.collect()
        assert 'dns' in facts
        assert facts['dns'] == {}
