# file lib/ansible/module_utils/facts/system/lsb.py:60-78
# lines [64]
# branches ['63->64', '75->66']

import os
import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_get_file_lines(mocker):
    return mocker.patch('ansible.module_utils.facts.system.lsb.get_file_lines')

def test_lsb_release_file_does_not_exist(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    collector = LSBFactCollector()
    lsb_facts = collector._lsb_release_file('/etc/lsb-release')
    assert lsb_facts == {}

def test_lsb_release_file_with_codename(mock_os_path_exists, mock_get_file_lines):
    mock_os_path_exists.return_value = True
    mock_get_file_lines.return_value = [
        'DISTRIB_ID=Ubuntu',
        'DISTRIB_RELEASE=20.04',
        'DISTRIB_DESCRIPTION="Ubuntu 20.04.1 LTS"',
        'DISTRIB_CODENAME=focal'
    ]
    collector = LSBFactCollector()
    lsb_facts = collector._lsb_release_file('/etc/lsb-release')
    assert lsb_facts == {
        'id': 'Ubuntu',
        'release': '20.04',
        'description': '"Ubuntu 20.04.1 LTS"',  # Keep the quotes as they are part of the mock return value
        'codename': 'focal'
    }
