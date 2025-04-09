# file lib/ansible/module_utils/facts/system/dns.py:25-67
# lines [30, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67]
# branches ['35->36', '35->67', '36->37', '36->38', '39->40', '39->41', '41->42', '41->46', '42->43', '42->44', '44->35', '44->45', '46->47', '46->49', '47->35', '47->48', '49->50', '49->53', '51->35', '51->52', '53->54', '53->57', '55->35', '55->56', '57->35', '57->58', '59->35', '59->60', '60->35', '60->61', '62->63', '62->64']

import pytest
from unittest.mock import mock_open, patch
from ansible.module_utils.facts.system.dns import DnsFactCollector

@pytest.fixture
def mock_file_content():
    content = (
        "# This is a comment\n"
        "; This is another comment\n"
        "nameserver 8.8.8.8\n"
        "nameserver 8.8.4.4\n"
        "domain example.com\n"
        "search example.org example.net\n"
        "sortlist 130.155.160.0\n"
        "options timeout:2 attempts:3 rotate\n"
    )
    return content

def test_dns_fact_collector(mock_file_content):
    with patch("ansible.module_utils.facts.system.dns.get_file_content", return_value=mock_file_content):
        collector = DnsFactCollector()
        facts = collector.collect()

    assert 'dns' in facts
    assert 'nameservers' in facts['dns']
    assert facts['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']
    assert 'domain' in facts['dns']
    assert facts['dns']['domain'] == 'example.com'
    assert 'search' in facts['dns']
    assert facts['dns']['search'] == ['example.org', 'example.net']
    assert 'sortlist' in facts['dns']
    assert facts['dns']['sortlist'] == ['130.155.160.0']
    assert 'options' in facts['dns']
    assert facts['dns']['options'] == {'timeout': '2', 'attempts': '3', 'rotate': True}
