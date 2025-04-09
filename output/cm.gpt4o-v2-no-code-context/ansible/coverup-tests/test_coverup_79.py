# file: lib/ansible/module_utils/facts/system/lsb.py:60-78
# asked: {"lines": [60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78], "branches": [[63, 64], [63, 66], [66, 67], [66, 78], [69, 70], [69, 71], [71, 72], [71, 73], [73, 74], [73, 75], [75, 66], [75, 76]]}
# gained: {"lines": [60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78], "branches": [[63, 64], [63, 66], [66, 67], [66, 78], [69, 70], [69, 71], [71, 72], [71, 73], [73, 74], [73, 75], [75, 76]]}

import os
import pytest
from unittest.mock import patch, mock_open

# Assuming the LSBFactCollector class is imported from the module
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_lsb_release_file_not_exists(lsb_collector, monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    result = lsb_collector._lsb_release_file('/fake/path/to/lsb-release')
    assert result == {}

def test_lsb_release_file_exists_empty(lsb_collector, monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=''))
    result = lsb_collector._lsb_release_file('/fake/path/to/lsb-release')
    assert result == {}

def test_lsb_release_file_with_data(lsb_collector, monkeypatch):
    lsb_data = """DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_DESCRIPTION="Ubuntu 20.04 LTS"
DISTRIB_CODENAME=focal"""
    
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=lsb_data))
    
    with patch('ansible.module_utils.facts.system.lsb.get_file_lines', return_value=lsb_data.splitlines()):
        result = lsb_collector._lsb_release_file('/fake/path/to/lsb-release')
    
    assert result == {
        'id': 'Ubuntu',
        'release': '20.04',
        'description': '"Ubuntu 20.04 LTS"',
        'codename': 'focal'
    }

def test_lsb_release_file_partial_data(lsb_collector, monkeypatch):
    lsb_data = """DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04"""
    
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=lsb_data))
    
    with patch('ansible.module_utils.facts.system.lsb.get_file_lines', return_value=lsb_data.splitlines()):
        result = lsb_collector._lsb_release_file('/fake/path/to/lsb-release')
    
    assert result == {
        'id': 'Ubuntu',
        'release': '20.04'
    }
