# file: lib/ansible/module_utils/common/sys_info.py:17-38
# asked: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}
# gained: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36]]}

import pytest
import platform
from ansible.module_utils import distro
from ansible.module_utils.common.sys_info import get_distribution

def test_get_distribution_amzn(monkeypatch):
    def mock_distro_id():
        return 'amzn'
    
    monkeypatch.setattr(distro, 'id', mock_distro_id)
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    
    assert get_distribution() == 'Amazon'

def test_get_distribution_rhel(monkeypatch):
    def mock_distro_id():
        return 'rhel'
    
    monkeypatch.setattr(distro, 'id', mock_distro_id)
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    
    assert get_distribution() == 'Redhat'

def test_get_distribution_other_linux(monkeypatch):
    def mock_distro_id():
        return ''
    
    monkeypatch.setattr(distro, 'id', mock_distro_id)
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    
    assert get_distribution() == 'OtherLinux'

def test_get_distribution_non_linux(monkeypatch):
    def mock_distro_id():
        return 'ubuntu'
    
    monkeypatch.setattr(distro, 'id', mock_distro_id)
    monkeypatch.setattr(platform, 'system', lambda: 'Windows')
    
    assert get_distribution() == 'Ubuntu'
