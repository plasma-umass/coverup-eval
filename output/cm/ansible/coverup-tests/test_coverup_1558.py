# file lib/ansible/module_utils/facts/system/user.py:26-53
# lines [34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53]
# branches []

import os
import pwd
import getpass
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_user():
    with patch('getpass.getuser', return_value='nobody') as mock:
        yield mock

@pytest.fixture
def mock_pwd():
    with patch('pwd.getpwnam') as mock_pwnam:
        mock_pwnam.side_effect = KeyError('No such user')
        with patch('pwd.getpwuid') as mock_pwuid:
            mock_pwuid.return_value = pwd.struct_passwd(('nobody', 'x', 65534, 65534, 'Unprivileged User,,,', '/nonexistent', '/usr/sbin/nologin'))
            yield mock_pwuid

@pytest.fixture
def mock_os():
    with patch('os.getuid', return_value=65534) as mock_uid, \
         patch('os.geteuid', return_value=65534) as mock_euid, \
         patch('os.getgid', return_value=65534) as mock_gid:
        yield mock_uid, mock_euid, mock_gid

def test_user_fact_collector(mock_getpass_user, mock_pwd, mock_os):
    collector = UserFactCollector()
    facts = collector.collect()

    assert facts['user_id'] == 'nobody'
    assert facts['user_uid'] == 65534
    assert facts['user_gid'] == 65534
    assert facts['user_gecos'] == 'Unprivileged User,,,'
    assert facts['user_dir'] == '/nonexistent'
    assert facts['user_shell'] == '/usr/sbin/nologin'
    assert facts['real_user_id'] == 65534
    assert facts['effective_user_id'] == 65534
    assert facts['real_group_id'] == 65534
    assert facts['effective_group_id'] == 65534
