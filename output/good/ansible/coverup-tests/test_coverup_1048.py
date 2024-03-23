# file lib/ansible/module_utils/facts/virtual/sysctl.py:23-24
# lines [23, 24]
# branches []

import pytest
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

class MockModule(object):
    def get_bin_path(self, bin_name):
        if bin_name == 'sysctl':
            return '/sbin/sysctl'
        return None

@pytest.fixture
def mock_module(mocker):
    mock = MockModule()
    mocker.patch.object(mock, 'get_bin_path', return_value='/sbin/sysctl')
    return mock

def test_detect_sysctl(mock_module):
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = mock_module
    mixin.detect_sysctl()
    mock_module.get_bin_path.assert_called_once_with('sysctl')
    assert mixin.sysctl_path == '/sbin/sysctl'
