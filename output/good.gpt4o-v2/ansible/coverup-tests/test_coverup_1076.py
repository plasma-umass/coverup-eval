# file: lib/ansible/executor/powershell/module_manifest.py:286-402
# asked: {"lines": [296, 297, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 335, 336, 337, 338, 339, 341, 342, 343, 344, 346, 347, 348, 349, 351, 352, 353, 354, 356, 357, 360, 361, 362, 367, 368, 370, 372, 373, 374, 376, 377, 378, 380, 381, 382, 383, 385, 386, 387, 388, 390, 391, 392, 393, 396, 397, 399, 401, 402], "branches": [[297, 300], [297, 302], [315, 316], [315, 326], [326, 327], [326, 335], [337, 338], [337, 346], [352, 353], [352, 360], [360, 361], [360, 367], [373, 374], [373, 376], [376, 377], [376, 380], [380, 381], [380, 385], [386, 387], [386, 390], [387, 386], [387, 388], [390, 391], [390, 393], [396, 397], [396, 399]]}
# gained: {"lines": [296, 297, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 335, 336, 337, 346, 347, 348, 349, 351, 352, 353, 354, 356, 357, 360, 367, 368, 370, 372, 373, 376, 377, 378, 380, 385, 386, 387, 390, 393, 396, 397, 399, 401, 402], "branches": [[297, 300], [315, 316], [326, 327], [337, 346], [352, 353], [360, 367], [373, 376], [376, 377], [376, 380], [380, 385], [386, 387], [386, 390], [387, 386], [390, 393], [396, 397]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper
from ansible import constants as C

@pytest.fixture
def mock_ps_module_dep_finder(monkeypatch):
    class MockPSModuleDepFinder:
        def __init__(self):
            self.ps_modules = {}
            self.exec_scripts = {}
            self.cs_utils_wrapper = {}
            self.cs_utils_module = {}
            self.ps_version = "5.1"
            self.os_version = "10.0"
            self.become = False

        def scan_module(self, module_data, fqn=None, wrapper=False, powershell=True):
            pass

        def scan_exec_script(self, name):
            self.exec_scripts[name] = b"script content"

        def _add_module(self, name, ext, fqn, optional, wrapper=False):
            pass

    monkeypatch.setattr("ansible.executor.powershell.module_manifest.PSModuleDepFinder", MockPSModuleDepFinder)
    return MockPSModuleDepFinder()

@pytest.fixture
def mock_config_get(monkeypatch):
    def mock_get_config_value(key, variables=None):
        if key == "WIN_ASYNC_STARTUP_TIMEOUT":
            return 30
        elif key == "COVERAGE_REMOTE_OUTPUT":
            return "coverage_output"
        elif key == "COVERAGE_REMOTE_PATHS":
            return ["path1", "path2"]
        return None

    monkeypatch.setattr(C.config, "get_config_value", mock_get_config_value)

@pytest.fixture
def mock_resource_from_fqcr(monkeypatch):
    def mock_resource(ref):
        return "runas"

    monkeypatch.setattr("ansible.utils.collection_loader.resource_from_fqcr", mock_resource)

def test_create_powershell_wrapper(mock_ps_module_dep_finder, mock_config_get, mock_resource_from_fqcr):
    b_module_data = b"module data"
    module_path = "module_path"
    module_args = ["arg1", "arg2"]
    environment = {"env1": "value1"}
    async_timeout = 10
    become = True
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = ["flag1"]
    substyle = "powershell"
    task_vars = {}
    module_fqn = "module_fqn"

    result = _create_powershell_wrapper(
        b_module_data, module_path, module_args, environment, async_timeout, become,
        become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn
    )

    assert result is not None
    assert b"exec_wrapper" in result
    assert b"async_wrapper" in result
    assert b"become_wrapper" in result
    assert b"coverage_wrapper" in result
    assert b"module_powershell_wrapper" in result
    assert b"module_entry" in result
    assert b"powershell_modules" in result
    assert b"csharp_utils" in result
    assert b"csharp_utils_module" in result
    assert b"async_jid" in result
    assert b"async_timeout_sec" in result
    assert b"async_startup_timeout" in result
    assert b"become_user" in result
    assert b"become_password" in result
    assert b"become_flags" in result
    assert b"min_ps_version" in result
    assert b"min_os_version" in result
    assert b"coverage" in result
