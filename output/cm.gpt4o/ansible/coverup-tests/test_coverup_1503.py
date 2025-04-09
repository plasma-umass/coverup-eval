# file lib/ansible/modules/dnf.py:978-993
# lines []
# branches ['984->993']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the DnfModule class is imported from ansible.modules.dnf
from ansible.modules.dnf import DnfModule

@pytest.fixture
def dnf_module():
    module = MagicMock()
    with patch('ansible.modules.dnf.get_best_parsable_locale', return_value='C'):
        dnf_module = DnfModule(module)
    dnf_module.with_modules = True
    dnf_module.module_base = MagicMock()
    dnf_module.base = MagicMock()
    return dnf_module

def test_is_module_installed_no_enabled_streams(dnf_module):
    module_spec = "testmodule"
    dnf_module.module_base._get_modules.return_value = ([], MagicMock(name="nsv", stream=None))
    dnf_module.base._moduleContainer.getEnabledStream.return_value = []

    result = dnf_module._is_module_installed(module_spec)
    
    assert result is False

def test_is_module_installed_stream_not_found(dnf_module):
    module_spec = "testmodule"
    nsv_mock = MagicMock(name="nsv", stream="teststream")
    dnf_module.module_base._get_modules.return_value = ([], nsv_mock)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["otherstream"]

    result = dnf_module._is_module_installed(module_spec)
    
    assert result is False

def test_is_module_installed_stream_found(dnf_module):
    module_spec = "testmodule"
    nsv_mock = MagicMock(name="nsv", stream="teststream")
    dnf_module.module_base._get_modules.return_value = ([], nsv_mock)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["teststream"]

    result = dnf_module._is_module_installed(module_spec)
    
    assert result is True

def test_is_module_installed_no_stream_provided(dnf_module):
    module_spec = "testmodule"
    nsv_mock = MagicMock(name="nsv", stream=None)
    dnf_module.module_base._get_modules.return_value = ([], nsv_mock)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["somestream"]

    result = dnf_module._is_module_installed(module_spec)
    
    assert result is True
