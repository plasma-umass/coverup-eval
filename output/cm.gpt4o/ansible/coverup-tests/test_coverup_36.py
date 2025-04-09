# file lib/ansible/module_utils/facts/system/selinux.py:40-91
# lines [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 90, 91]
# branches ['47->48', '47->54', '56->57', '56->59', '68->69', '68->71', '83->84', '83->86']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the module is imported as follows:
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector, HAVE_SELINUX, SELINUX_MODE_DICT

@pytest.fixture
def mock_selinux():
    with patch('ansible.module_utils.facts.system.selinux.selinux') as mock_selinux:
        yield mock_selinux

def test_selinux_library_missing():
    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False):
        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['status'] == 'Missing selinux Python library'
        assert facts['selinux_python_present'] == False

def test_selinux_disabled(mock_selinux):
    mock_selinux.is_selinux_enabled.return_value = False
    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True):
        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['status'] == 'disabled'
        assert facts['selinux_python_present'] == True

def test_selinux_enabled(mock_selinux):
    mock_selinux.is_selinux_enabled.return_value = True
    mock_selinux.security_policyvers.return_value = 30
    mock_selinux.selinux_getenforcemode.return_value = (0, 1)
    mock_selinux.security_getenforce.return_value = 1
    mock_selinux.selinux_getpolicytype.return_value = (0, 'targeted')

    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True):
        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['status'] == 'enabled'
        assert facts['selinux']['policyvers'] == 30
        assert facts['selinux']['config_mode'] == SELINUX_MODE_DICT[1]
        assert facts['selinux']['mode'] == SELINUX_MODE_DICT[1]
        assert facts['selinux']['type'] == 'targeted'
        assert facts['selinux_python_present'] == True

def test_selinux_enabled_with_exceptions(mock_selinux):
    mock_selinux.is_selinux_enabled.return_value = True
    mock_selinux.security_policyvers.side_effect = AttributeError
    mock_selinux.selinux_getenforcemode.side_effect = OSError
    mock_selinux.security_getenforce.side_effect = AttributeError
    mock_selinux.selinux_getpolicytype.side_effect = OSError

    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True):
        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['status'] == 'enabled'
        assert facts['selinux']['policyvers'] == 'unknown'
        assert facts['selinux']['config_mode'] == 'unknown'
        assert facts['selinux']['mode'] == 'unknown'
        assert facts['selinux']['type'] == 'unknown'
        assert facts['selinux_python_present'] == True
