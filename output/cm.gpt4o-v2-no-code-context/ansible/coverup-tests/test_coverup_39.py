# file: lib/ansible/module_utils/facts/system/lsb.py:32-58
# asked: {"lines": [32, 33, 35, 36, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58], "branches": [[35, 36], [35, 38], [39, 40], [39, 42], [42, 43], [42, 58], [43, 44], [43, 45], [47, 48], [47, 49], [49, 50], [49, 51], [51, 52], [51, 53], [53, 54], [53, 55], [55, 42], [55, 56]]}
# gained: {"lines": [32, 33, 35, 36, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58], "branches": [[35, 36], [35, 38], [39, 40], [39, 42], [42, 43], [42, 58], [43, 44], [43, 45], [47, 48], [47, 49], [49, 50], [49, 51], [51, 52], [51, 53], [53, 54], [53, 55], [55, 56]]}

import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_lsb_release_bin_no_path(lsb_collector, mock_module):
    lsb_path = None
    result = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    assert result == {}

def test_lsb_release_bin_command_failure(lsb_collector, mock_module):
    lsb_path = "/usr/bin/lsb_release"
    mock_module.run_command.return_value = (1, "", "error")
    result = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    assert result == {}

def test_lsb_release_bin_success(lsb_collector, mock_module):
    lsb_path = "/usr/bin/lsb_release"
    output = (
        "LSB Version:    core-4.1-amd64:core-4.1-noarch\n"
        "Distributor ID: Ubuntu\n"
        "Description:    Ubuntu 20.04.1 LTS\n"
        "Release:        20.04\n"
        "Codename:       focal\n"
    )
    mock_module.run_command.return_value = (0, output, "")
    result = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    assert result == {
        'release': '20.04',
        'id': 'Ubuntu',
        'description': 'Ubuntu 20.04.1 LTS',
        'codename': 'focal'
    }

def test_lsb_release_bin_partial_output(lsb_collector, mock_module):
    lsb_path = "/usr/bin/lsb_release"
    output = (
        "LSB Version:    core-4.1-amd64:core-4.1-noarch\n"
        "Distributor ID: Ubuntu\n"
        "Release:        20.04\n"
    )
    mock_module.run_command.return_value = (0, output, "")
    result = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    assert result == {
        'release': '20.04',
        'id': 'Ubuntu'
    }

def test_lsb_release_bin_malformed_output(lsb_collector, mock_module):
    lsb_path = "/usr/bin/lsb_release"
    output = (
        "LSB Version:    core-4.1-amd64:core-4.1-noarch\n"
        "Distributor ID Ubuntu\n"  # Malformed line
        "Description:    Ubuntu 20.04.1 LTS\n"
        "Release:        20.04\n"
        "Codename:       focal\n"
    )
    mock_module.run_command.return_value = (0, output, "")
    result = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    assert result == {
        'release': '20.04',
        'description': 'Ubuntu 20.04.1 LTS',
        'codename': 'focal'
    }
