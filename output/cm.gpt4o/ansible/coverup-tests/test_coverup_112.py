# file lib/ansible/module_utils/facts/system/lsb.py:60-78
# lines [60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78]
# branches ['63->64', '63->66', '66->67', '66->78', '69->70', '69->71', '71->72', '71->73', '73->74', '73->75', '75->66', '75->76']

import os
import pytest
from unittest import mock
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_get_file_lines(mocker):
    return mocker.patch('ansible.module_utils.facts.system.lsb.get_file_lines')

def test_lsb_release_file_exists(mock_os_path_exists, mock_get_file_lines):
    mock_os_path_exists.return_value = True
    mock_get_file_lines.return_value = [
        'DISTRIB_ID=Ubuntu\n',
        'DISTRIB_RELEASE=20.04\n',
        'DISTRIB_DESCRIPTION="Ubuntu 20.04 LTS"\n',
        'DISTRIB_CODENAME=focal\n'
    ]

    collector = LSBFactCollector()
    lsb_facts = collector._lsb_release_file('/etc/lsb-release')

    assert lsb_facts['id'] == 'Ubuntu'
    assert lsb_facts['release'] == '20.04'
    assert lsb_facts['description'] == '"Ubuntu 20.04 LTS"'
    assert lsb_facts['codename'] == 'focal'

def test_lsb_release_file_not_exists(mock_os_path_exists):
    mock_os_path_exists.return_value = False

    collector = LSBFactCollector()
    lsb_facts = collector._lsb_release_file('/etc/lsb-release')

    assert lsb_facts == {}
