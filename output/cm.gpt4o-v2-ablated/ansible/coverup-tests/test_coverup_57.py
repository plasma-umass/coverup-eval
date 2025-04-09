# file: lib/ansible/module_utils/common/network.py:64-83
# asked: {"lines": [64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 77, 78, 79, 81, 82, 83], "branches": [[67, 68], [67, 69], [78, 79], [78, 81], [81, 82], [81, 83]]}
# gained: {"lines": [64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 77, 78, 79, 81, 82, 83], "branches": [[67, 68], [67, 69], [78, 79], [78, 81], [81, 82], [81, 83]]}

import pytest
from ansible.module_utils.common.network import to_subnet

def test_to_subnet_valid_masklen(monkeypatch):
    def mock_is_masklen(mask):
        return True

    def mock_to_netmask(mask):
        return '255.255.255.0'

    monkeypatch.setattr('ansible.module_utils.common.network.is_masklen', mock_is_masklen)
    monkeypatch.setattr('ansible.module_utils.common.network.to_netmask', mock_to_netmask)

    result = to_subnet('192.168.1.1', '24')
    assert result == '192.168.1.0/24'

def test_to_subnet_invalid_masklen(monkeypatch):
    def mock_is_masklen(mask):
        return False

    def mock_to_masklen(mask):
        return 24

    monkeypatch.setattr('ansible.module_utils.common.network.is_masklen', mock_is_masklen)
    monkeypatch.setattr('ansible.module_utils.common.network.to_masklen', mock_to_masklen)

    result = to_subnet('192.168.1.1', '255.255.255.0')
    assert result == '192.168.1.0/24'

def test_to_subnet_dotted_notation(monkeypatch):
    def mock_is_masklen(mask):
        return True

    def mock_to_netmask(mask):
        return '255.255.255.0'

    monkeypatch.setattr('ansible.module_utils.common.network.is_masklen', mock_is_masklen)
    monkeypatch.setattr('ansible.module_utils.common.network.to_netmask', mock_to_netmask)

    result = to_subnet('192.168.1.1', '24', dotted_notation=True)
    assert result == '192.168.1.0 255.255.255.0'
