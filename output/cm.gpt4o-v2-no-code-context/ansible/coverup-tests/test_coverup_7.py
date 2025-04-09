# file: lib/ansible/module_utils/facts/system/dns.py:25-67
# asked: {"lines": [25, 26, 27, 29, 30, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67], "branches": [[35, 36], [35, 67], [36, 37], [36, 38], [39, 40], [39, 41], [41, 42], [41, 46], [42, 43], [42, 44], [44, 35], [44, 45], [46, 47], [46, 49], [47, 35], [47, 48], [49, 50], [49, 53], [51, 35], [51, 52], [53, 54], [53, 57], [55, 35], [55, 56], [57, 35], [57, 58], [59, 35], [59, 60], [60, 35], [60, 61], [62, 63], [62, 64]]}
# gained: {"lines": [25, 26, 27, 29, 30, 33, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 67], "branches": [[35, 36], [35, 67], [36, 37], [36, 38], [39, 41], [41, 42], [41, 46], [42, 43], [42, 44], [44, 35], [44, 45], [46, 47], [46, 49], [47, 48], [49, 50], [49, 53], [51, 35], [51, 52], [53, 54], [53, 57], [55, 35], [55, 56], [57, 58], [59, 60], [60, 35], [60, 61], [62, 64]]}

import pytest
from ansible.module_utils.facts.system.dns import DnsFactCollector
from unittest.mock import patch

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.dns.get_file_content') as mock:
        yield mock

def test_collect_nameservers(mock_get_file_content):
    mock_get_file_content.return_value = "nameserver 8.8.8.8\nnameserver 8.8.4.4"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'nameservers' in result['dns']
    assert result['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']

def test_collect_domain(mock_get_file_content):
    mock_get_file_content.return_value = "domain example.com"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'domain' in result['dns']
    assert result['dns']['domain'] == 'example.com'

def test_collect_search(mock_get_file_content):
    mock_get_file_content.return_value = "search example.com sub.example.com"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'search' in result['dns']
    assert result['dns']['search'] == ['example.com', 'sub.example.com']

def test_collect_sortlist(mock_get_file_content):
    mock_get_file_content.return_value = "sortlist 192.168.1.0/255.255.255.0"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'sortlist' in result['dns']
    assert result['dns']['sortlist'] == ['192.168.1.0/255.255.255.0']

def test_collect_options(mock_get_file_content):
    mock_get_file_content.return_value = "options timeout:2 attempts:3"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'options' in result['dns']
    assert result['dns']['options'] == {'timeout': '2', 'attempts': '3'}

def test_collect_empty_lines_and_comments(mock_get_file_content):
    mock_get_file_content.return_value = "# This is a comment\n; Another comment\n\nnameserver 8.8.8.8"
    collector = DnsFactCollector()
    result = collector.collect()
    assert 'dns' in result
    assert 'nameservers' in result['dns']
    assert result['dns']['nameservers'] == ['8.8.8.8']
