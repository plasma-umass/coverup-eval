# file: lib/ansible/module_utils/facts/system/lsb.py:32-58
# asked: {"lines": [44], "branches": [[43, 44], [55, 42]]}
# gained: {"lines": [44], "branches": [[43, 44], [55, 42]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_lsb_release_bin_no_lsb_path(lsb_collector, mock_module):
    result = lsb_collector._lsb_release_bin(None, mock_module)
    assert result == {}

def test_lsb_release_bin_command_fails(lsb_collector, mock_module):
    mock_module.run_command.return_value = (1, '', '')
    result = lsb_collector._lsb_release_bin('/fake/path', mock_module)
    assert result == {}

def test_lsb_release_bin_parsing(lsb_collector, mock_module):
    output = (
        "LSB Version:    1.4\n"
        "Distributor ID: Ubuntu\n"
        "Description:    Ubuntu 20.04.1 LTS\n"
        "Release:        20.04\n"
        "Codename:       focal\n"
        "\n"
        "Some other info: value\n"
    )
    mock_module.run_command.return_value = (0, output, '')
    result = lsb_collector._lsb_release_bin('/fake/path', mock_module)
    assert result == {
        'release': '20.04',
        'id': 'Ubuntu',
        'description': 'Ubuntu 20.04.1 LTS',
        'codename': 'focal'
    }

def test_lsb_release_bin_empty_line(lsb_collector, mock_module):
    output = (
        "LSB Version:    1.4\n"
        "\n"
        "Distributor ID: Ubuntu\n"
    )
    mock_module.run_command.return_value = (0, output, '')
    result = lsb_collector._lsb_release_bin('/fake/path', mock_module)
    assert result == {
        'release': '1.4',
        'id': 'Ubuntu'
    }
