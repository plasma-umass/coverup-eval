# file: lib/ansible/executor/powershell/module_manifest.py:164-235
# asked: {"lines": [164, 165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 197, 198, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 175], [174, 177], [185, 186], [185, 194], [187, 188], [187, 192], [188, 189], [188, 190], [200, 201], [200, 203], [208, 210], [208, 212], [214, 215], [214, 222], [215, 216], [215, 218], [228, 229], [228, 231], [231, 232], [231, 234]]}
# gained: {"lines": [164, 165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 194, 195, 197, 198, 199, 200, 203, 204, 207, 208, 212, 213, 214, 215, 218, 219, 224, 225, 226, 228, 229, 231, 234, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 175], [174, 177], [185, 194], [200, 203], [208, 212], [214, 215], [215, 218], [228, 229], [228, 231], [231, 234]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder, AnsibleError
import os
import errno
import pkgutil
from importlib import import_module

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_add_module_builtin_util(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin', lambda name, ext: 'mock_path')
    monkeypatch.setattr('ansible.executor.powershell.module_manifest._slurp', lambda path: b'mock_data')
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_bytes', lambda x: x)
    
    ps_module_dep_finder.ps_modules = {}
    ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'Ansible.Builtin', False)
    
    assert 'Ansible.Builtin' in ps_module_dep_finder.ps_modules
    assert ps_module_dep_finder.ps_modules['Ansible.Builtin']['data'] == b'mock_data'
    assert ps_module_dep_finder.ps_modules['Ansible.Builtin']['path'] == 'mock_path'

def test_add_module_collection_util(ps_module_dep_finder, monkeypatch):
    mock_module = MagicMock()
    mock_module.__path__ = ['mock_path']
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', lambda name: mock_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.pkgutil.get_data', lambda pkg, res: b'mock_data')
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_bytes', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)
    
    ps_module_dep_finder.cs_utils_module = {}
    ps_module_dep_finder._add_module('Collection.Util', '.ps1', 'Collection.Util', False)
    
    assert 'Collection.Util' in ps_module_dep_finder.cs_utils_module
    assert ps_module_dep_finder.cs_utils_module['Collection.Util']['data'] == b'mock_data'
    assert ps_module_dep_finder.cs_utils_module['Collection.Util']['path'] == os.path.join('mock_path', 'Util.ps1')

def test_add_module_optional_not_found(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin', lambda name, ext: None)
    
    ps_module_dep_finder._add_module('Ansible.Optional', '.psm1', 'Ansible.Optional', True)
    # No assertion needed, just ensuring no exception is raised

def test_add_module_non_optional_not_found(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin', lambda name, ext: None)
    
    with pytest.raises(AnsibleError, match="Could not find imported module support code for 'Ansible.NonOptional'"):
        ps_module_dep_finder._add_module('Ansible.NonOptional', '.psm1', 'Ansible.NonOptional', False)

def test_add_module_import_error(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise ImportError("No package data found")
    
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)
    
    with pytest.raises(AnsibleError, match="Could not find collection imported module support code for 'Collection.Util'"):
        ps_module_dep_finder._add_module('Collection.Util', '.ps1', 'Collection.Util', False)

def test_add_module_os_error(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise OSError(errno.ENOENT, "No such file or directory")
    
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)
    
    with pytest.raises(AnsibleError, match="Could not find collection imported module support code for 'Collection.Util'"):
        ps_module_dep_finder._add_module('Collection.Util', '.ps1', 'Collection.Util', False)
