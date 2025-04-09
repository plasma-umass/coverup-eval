# file lib/ansible/parsing/utils/addresses.py:170-216
# lines [214]
# branches ['213->214']

import pytest
from ansible.parsing.utils.addresses import parse_address, AnsibleParserError

def test_parse_address_with_ranges_not_allowed():
    address = "foo[1:3]"
    with pytest.raises(AnsibleParserError, match="Detected range in host but was asked to ignore ranges"):
        parse_address(address, allow_ranges=False)

def test_parse_address_with_ranges_allowed():
    address = "foo[1:3]"
    host, port = parse_address(address, allow_ranges=True)
    assert host == "foo[1:3]"
    assert port is None
