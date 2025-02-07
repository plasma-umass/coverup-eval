# file: lib/ansible/executor/powershell/module_manifest.py:286-402
# asked: {"lines": [338, 339, 341, 342, 343, 344, 361, 362, 374, 381, 382, 383, 388, 391, 392], "branches": [[297, 302], [315, 326], [326, 335], [337, 338], [352, 360], [360, 361], [373, 374], [380, 381], [387, 388], [390, 391], [396, 399]]}
# gained: {"lines": [361, 362, 374, 381, 382, 383, 388, 391, 392], "branches": [[297, 302], [315, 326], [326, 335], [352, 360], [360, 361], [373, 374], [380, 381], [387, 388], [390, 391], [396, 399]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper, PSModuleDepFinder
from ansible.errors import AnsibleError

@pytest.fixture
def mock_finder(monkeypatch):
    finder = PSModuleDepFinder()
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.PSModuleDepFinder', lambda: finder)
    return finder

def test_create_powershell_wrapper_script_substyle(mock_finder):
    b_module_data = b"test data"
    module_path = "test_path"
    module_args = {}
    environment = {}
    async_timeout = 0
    become = False
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = []
    substyle = "script"
    task_vars = {}
    module_fqn = "test_fqn"

    with patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b""):
        result = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn)
    
    assert "module_script_wrapper" in result.decode()

def test_create_powershell_wrapper_async_timeout(mock_finder):
    b_module_data = b"test data"
    module_path = "test_path"
    module_args = {}
    environment = {}
    async_timeout = 10
    become = False
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = []
    substyle = "powershell"
    task_vars = {}

    with patch('random.randint', return_value=123456789):
        with patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b""):
            result = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, "test_fqn")
    
    assert "async_watchdog" in result.decode()
    assert "async_wrapper" in result.decode()
    assert '"async_jid": "123456789"' in result.decode()

def test_create_powershell_wrapper_become(mock_finder):
    b_module_data = b"test data"
    module_path = "test_path"
    module_args = {}
    environment = {}
    async_timeout = 0
    become = True
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = []
    substyle = "powershell"
    task_vars = {}

    with patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b""):
        result = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, "test_fqn")
    
    assert "become_wrapper" in result.decode()
    assert '"become_user": "user"' in result.decode()

def test_create_powershell_wrapper_coverage(mock_finder):
    b_module_data = b"test data"
    module_path = "test_path"
    module_args = {}
    environment = {}
    async_timeout = 0
    become = False
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = []
    substyle = "powershell"
    task_vars = {"COVERAGE_REMOTE_OUTPUT": "output_path", "COVERAGE_REMOTE_PATHS": "path_filter"}

    with patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b""):
        with patch('ansible.executor.powershell.module_manifest.C.config.get_config_value', side_effect=lambda key, variables=None: variables.get(key)):
            result = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, "test_fqn")
    
    assert "coverage_wrapper" in result.decode()
    assert '"output": "output_path"' in result.decode()
    assert '"path_filter": "path_filter"' in result.decode()

def test_create_powershell_wrapper_cs_utils(mock_finder):
    b_module_data = b"test data"
    module_path = "test_path"
    module_args = {}
    environment = {}
    async_timeout = 0
    become = False
    become_method = "runas"
    become_user = "user"
    become_password = "password"
    become_flags = []
    substyle = "powershell"
    task_vars = {}

    mock_finder.cs_utils_wrapper = {"test_util": {"data": b"util data"}}
    with patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b""):
        result = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, "test_fqn")
    
    assert "Ansible.ModuleUtils.AddType" in result.decode()
    assert '"test_util": "dXRpbCBkYXRh"' in result.decode()  # base64 encoded "util data"
