# file lib/ansible/galaxy/user_agent.py:13-23
# lines [13, 16, 17, 18, 19, 20, 21, 22]
# branches []

import sys
import platform
from unittest.mock import patch, MagicMock
import pytest

# Assuming the ansible_version is defined somewhere in the module
# If not, you would need to mock or define it as well
from ansible.galaxy.user_agent import user_agent, ansible_version

def test_user_agent():
    fake_version_info = MagicMock(major=3, minor=8, micro=6)
    with patch.object(platform, 'system', return_value='TestOS'), \
         patch.object(sys, 'version_info', fake_version_info):
        ua = user_agent()
        assert ua == f"ansible-galaxy/{ansible_version} (TestOS; python:3.8.6)"
