# file: lib/ansible/module_utils/facts/system/distribution.py:408-424
# asked: {"lines": [408, 409, 411, 413, 414, 417, 418, 419, 420, 422, 424], "branches": [[413, 414], [413, 422], [414, 417], [414, 418], [419, 420], [419, 424]]}
# gained: {"lines": [408, 409, 411, 413, 414, 417, 418, 419, 420, 422, 424], "branches": [[413, 414], [413, 422], [414, 417], [414, 418], [419, 420]]}

import pytest
import re
from ansible.module_utils.facts.system.distribution import DistributionFiles
from ansible.module_utils.common.sys_info import get_distribution

class MockedDistribution:
    def __init__(self, distro_name):
        self.distro_name = distro_name

    def id(self):
        return self.distro_name

@pytest.fixture
def mock_distro(monkeypatch):
    def mock_get_distribution():
        return "coreos"
    
    monkeypatch.setattr("ansible.module_utils.common.sys_info.distro", MockedDistribution("coreos"))
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", mock_get_distribution)

@pytest.fixture
def dist_files(mock_distro):
    class MockModule:
        pass
    
    return DistributionFiles(MockModule())

def test_parse_distribution_file_Coreos_no_data(dist_files):
    result, facts = dist_files.parse_distribution_file_Coreos("name", "", "path", {})
    assert result == False
    assert facts == {}

def test_parse_distribution_file_Coreos_with_data(dist_files):
    data = 'GROUP="stable"'
    result, facts = dist_files.parse_distribution_file_Coreos("name", data, "path", {})
    assert result == True
    assert facts == {"distribution_release": "stable"}

def test_parse_distribution_file_Coreos_not_coreos(monkeypatch):
    def mock_get_distribution():
        return "ubuntu"
    
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", mock_get_distribution)
    
    class MockModule:
        pass
    
    dist_files = DistributionFiles(MockModule())
    result, facts = dist_files.parse_distribution_file_Coreos("name", "data", "path", {})
    assert result == False
    assert facts == {}
