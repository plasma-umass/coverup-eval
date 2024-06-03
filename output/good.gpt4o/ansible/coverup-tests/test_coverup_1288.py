# file lib/ansible/module_utils/facts/system/user.py:26-53
# lines [40, 41]
# branches []

import pytest
import getpass
import pwd
import os
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpwnam(mocker):
    # Mock getpwnam to raise KeyError
    return mocker.patch('pwd.getpwnam', side_effect=KeyError)

@pytest.fixture
def mock_getpwuid(mocker):
    # Mock getpwuid to return a fake user entry
    fake_pwent = pwd.struct_passwd(('fakeuser', 'x', 1000, 1000, 'Fake User', '/home/fakeuser', '/bin/bash'))
    return mocker.patch('pwd.getpwuid', return_value=fake_pwent)

def test_collect_user_facts_keyerror(mock_getpwnam, mock_getpwuid):
    collector = UserFactCollector()
    facts = collector.collect()

    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == 1000
    assert facts['user_gid'] == 1000
    assert facts['user_gecos'] == 'Fake User'
    assert facts['user_dir'] == '/home/fakeuser'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getgid()
