# file: lib/ansible/galaxy/user_agent.py:13-23
# asked: {"lines": [13, 16, 17, 18, 19, 20, 21, 22], "branches": []}
# gained: {"lines": [13, 16, 17, 18, 19, 20, 21, 22], "branches": []}

import pytest
import platform
import sys
from ansible.module_utils.ansible_release import __version__ as ansible_version
from ansible.galaxy.user_agent import user_agent

class MockVersionInfo:
    def __init__(self, major, minor, micro):
        self.major = major
        self.minor = minor
        self.micro = micro

def test_user_agent(monkeypatch):
    # Mock platform.system
    monkeypatch.setattr(platform, "system", lambda: "TestOS")
    
    # Mock sys.version_info
    mock_version_info = MockVersionInfo(3, 9, 1)
    monkeypatch.setattr(sys, "version_info", mock_version_info)
    
    expected_user_agent = u"ansible-galaxy/{ansible_version} (TestOS; python:3.9.1)".format(
        ansible_version=ansible_version,
    )
    
    result = user_agent()
    
    assert result == expected_user_agent
