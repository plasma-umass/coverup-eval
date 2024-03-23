# file lib/ansible/parsing/utils/addresses.py:170-216
# lines [192, 193, 194, 208, 214]
# branches ['191->192', '207->208', '213->214']

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.parsing.utils.addresses import parse_address
from unittest.mock import Mock, MagicMock

@pytest.fixture
def mock_patterns(mocker):
    patterns = {
        'bracketed_hostport': Mock(),
        'hostport': Mock(),
        'ipv4': Mock(),
        'ipv6': Mock(),
        'hostname': Mock(),
    }
    mocker.patch('ansible.parsing.utils.addresses.patterns', patterns)
    return patterns

def test_parse_address_invalid_hostname(mock_patterns):
    mock_patterns['bracketed_hostport'].match.return_value = None
    mock_patterns['hostport'].match.return_value = None
    mock_patterns['ipv4'].match.return_value = None
    mock_patterns['ipv6'].match.return_value = None
    mock_patterns['hostname'].match.return_value = None

    with pytest.raises(AnsibleError) as excinfo:
        parse_address("invalid_hostname")
    assert "Not a valid network hostname" in str(excinfo.value)

def test_parse_address_ignore_ranges(mock_patterns):
    mock_patterns['bracketed_hostport'].match.return_value = None
    mock_patterns['hostport'].match.return_value = None
    mock_patterns['ipv4'].match.return_value = None
    mock_patterns['ipv6'].match.return_value = None
    mock_patterns['hostname'].match.return_value = Mock(groups=lambda: ('hostname[0:1]',))

    with pytest.raises(AnsibleParserError) as excinfo:
        parse_address("hostname[0:1]", allow_ranges=False)
    assert "Detected range in host but was asked to ignore ranges" in str(excinfo.value)

def test_parse_address_with_port(mock_patterns):
    mock_patterns['bracketed_hostport'].match.return_value = None
    mock_patterns['hostport'].match.side_effect = lambda x: MagicMock(groups=lambda: (x.split(':')[0], x.split(':')[1])) if ':' in x else None
    mock_patterns['ipv4'].match.return_value = None
    mock_patterns['ipv6'].match.return_value = None
    mock_patterns['hostname'].match.return_value = Mock(groups=lambda: ('hostname',))

    host, port = parse_address("hostname:1234")
    assert host == "hostname"
    assert port == 1234
