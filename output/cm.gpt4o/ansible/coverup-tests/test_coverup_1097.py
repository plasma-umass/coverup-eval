# file lib/ansible/modules/dnf.py:978-993
# lines [978, 979, 980, 981, 982, 984, 985, 986, 987, 989, 991, 993]
# branches ['979->980', '979->993', '984->985', '984->993', '985->986', '985->991', '986->987', '986->989']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the DnfModule class is imported from ansible.modules.dnf
from ansible.modules.dnf import DnfModule

@pytest.fixture
def dnf_module():
    module = MagicMock()
    module.get_bin_path.return_value = "/usr/bin/locale"
    module.run_command.return_value = (0, "C.utf8\nen_US.utf8\nC\nPOSIX", "")
    dnf_module = DnfModule(module)
    dnf_module.with_modules = True
    dnf_module.module_base = MagicMock()
    dnf_module.base = MagicMock()
    return dnf_module

def test_is_module_installed_with_stream(dnf_module):
    module_spec = "testmodule:stream"
    nsv = MagicMock()
    nsv.name = "testmodule"
    nsv.stream = "stream"
    
    dnf_module.module_base._get_modules.return_value = ([], nsv)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["stream"]
    
    assert dnf_module._is_module_installed(module_spec) == True

def test_is_module_installed_without_stream(dnf_module):
    module_spec = "testmodule"
    nsv = MagicMock()
    nsv.name = "testmodule"
    nsv.stream = None
    
    dnf_module.module_base._get_modules.return_value = ([], nsv)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["stream"]
    
    assert dnf_module._is_module_installed(module_spec) == True

def test_is_module_installed_stream_not_found(dnf_module):
    module_spec = "testmodule:stream"
    nsv = MagicMock()
    nsv.name = "testmodule"
    nsv.stream = "stream"
    
    dnf_module.module_base._get_modules.return_value = ([], nsv)
    dnf_module.base._moduleContainer.getEnabledStream.return_value = ["otherstream"]
    
    assert dnf_module._is_module_installed(module_spec) == False

def test_is_module_installed_no_modules(dnf_module):
    module_spec = "testmodule"
    nsv = MagicMock()
    nsv.name = "testmodule"
    nsv.stream = None
    
    dnf_module.with_modules = False
    
    assert dnf_module._is_module_installed(module_spec) == False
