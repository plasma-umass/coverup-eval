# file: lib/ansible/executor/powershell/module_manifest.py:286-402
# asked: {"lines": [296, 297, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 335, 336, 337, 338, 339, 341, 342, 343, 344, 346, 347, 348, 349, 351, 352, 353, 354, 356, 357, 360, 361, 362, 367, 368, 370, 372, 373, 374, 376, 377, 378, 380, 381, 382, 383, 385, 386, 387, 388, 390, 391, 392, 393, 396, 397, 399, 401, 402], "branches": [[297, 300], [297, 302], [315, 316], [315, 326], [326, 327], [326, 335], [337, 338], [337, 346], [352, 353], [352, 360], [360, 361], [360, 367], [373, 374], [373, 376], [376, 377], [376, 380], [380, 381], [380, 385], [386, 387], [386, 390], [387, 386], [387, 388], [390, 391], [390, 393], [396, 397], [396, 399]]}
# gained: {"lines": [296, 297, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 335, 336, 337, 346, 347, 348, 349, 351, 352, 353, 354, 356, 357, 360, 367, 368, 370, 372, 373, 376, 377, 378, 380, 385, 386, 387, 390, 393, 396, 397, 399, 401, 402], "branches": [[297, 300], [315, 316], [326, 327], [337, 346], [352, 353], [360, 367], [373, 376], [376, 377], [376, 380], [380, 385], [386, 387], [386, 390], [387, 386], [390, 393], [396, 397]]}

import pytest
import base64
import json
import random
from unittest.mock import patch, MagicMock
from ansible import constants as C
from ansible.module_utils._text import to_bytes, to_text
from ansible.utils.collection_loader import resource_from_fqcr
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper

class MockPSModuleDepFinder:
    def __init__(self):
        self.ps_modules = dict()
        self.exec_scripts = dict()
        self.cs_utils_wrapper = dict()
        self.cs_utils_module = dict()
        self.ps_version = None
        self.os_version = None
        self.become = False

    def scan_module(self, module_data, fqn=None, wrapper=False, powershell=True):
        pass

    def scan_exec_script(self, name):
        self.exec_scripts[name] = b""

    def _add_module(self, name, ext, fqn, optional, wrapper=False):
        pass

@pytest.fixture
def mock_finder(monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.PSModuleDepFinder', MockPSModuleDepFinder)

@pytest.fixture
def mock_config(monkeypatch):
    mock_get_config_value = MagicMock(side_effect=lambda key, variables=None: {
        "WIN_ASYNC_STARTUP_TIMEOUT": 30,
        "COVERAGE_REMOTE_OUTPUT": "/path/to/output",
        "COVERAGE_REMOTE_PATHS": ["/path/to/coverage"]
    }.get(key, None))
    monkeypatch.setattr(C.config, 'get_config_value', mock_get_config_value)

def test_create_powershell_wrapper(mock_finder, mock_config):
    b_module_data = to_bytes("dummy module data")
    module_path = "dummy_module_path"
    module_args = ["arg1", "arg2"]
    environment = {"ENV_VAR": "value"}
    async_timeout = 10
    become = True
    become_method = "runas"
    become_user = "admin"
    become_password = "password"
    become_flags = ["flag1", "flag2"]
    substyle = "powershell"
    task_vars = {}
    module_fqn = "dummy.fqn"

    result = _create_powershell_wrapper(
        b_module_data, module_path, module_args, environment, async_timeout, become,
        become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn
    )

    assert result is not None
    assert isinstance(result, bytes)
    assert b'\0\0\0\0' in result

    exec_manifest = json.loads(to_text(result.split(b'\0\0\0\0')[1]))
    assert exec_manifest["module_entry"] == to_text(base64.b64encode(b_module_data))
    assert exec_manifest["module_args"] == module_args
    assert exec_manifest["environment"] == environment
    assert exec_manifest["async_jid"] is not None
    assert exec_manifest["async_timeout_sec"] == async_timeout
    assert exec_manifest["async_startup_timeout"] == 30
    assert exec_manifest["become_user"] == become_user
    assert exec_manifest["become_password"] == become_password
    assert exec_manifest["become_flags"] == become_flags
    assert exec_manifest["min_ps_version"] is None
    assert exec_manifest["min_os_version"] is None
    assert "coverage" in exec_manifest
    assert exec_manifest["coverage"]["output"] == "/path/to/output"
    assert exec_manifest["coverage"]["path_filter"] == ["/path/to/coverage"]
