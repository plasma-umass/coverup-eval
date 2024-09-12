# file: lib/ansible/executor/powershell/module_manifest.py:164-235
# asked: {"lines": [165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 197, 198, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 175], [174, 177], [185, 186], [185, 194], [187, 188], [187, 192], [188, 189], [188, 190], [200, 201], [200, 203], [208, 210], [208, 212], [214, 215], [214, 222], [215, 216], [215, 218], [228, 229], [228, 231], [231, 232], [231, 234]]}
# gained: {"lines": [165, 167, 169, 171, 173, 174, 177, 178, 180, 184, 185, 194, 195, 197, 198, 199, 200, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 224, 225, 226, 228, 229, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 177], [185, 194], [200, 203], [208, 210], [208, 212], [214, 215], [215, 216], [215, 218], [228, 229]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
import os
import errno

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder.ps_modules = {}
    finder.cs_utils_wrapper = {}
    finder.cs_utils_module = {}
    return finder

def test_add_module_builtin_util(ps_module_dep_finder, monkeypatch):
    def mock_find_plugin(name, ext):
        return '/fake/path/to/plugin'

    def mock_slurp(path):
        return b'fake data'

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin', mock_find_plugin)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest._slurp', mock_slurp)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_bytes', lambda x: x)

    ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'fqn', optional=False)
    assert 'Ansible.Builtin' in ps_module_dep_finder.ps_modules

def test_add_module_builtin_util_not_found(ps_module_dep_finder, monkeypatch):
    def mock_find_plugin(name, ext):
        return None

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin', mock_find_plugin)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x: x)

    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'fqn', optional=False)

def test_add_module_collection_util(ps_module_dep_finder, monkeypatch):
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path/to/module']

    def mock_import_module(name):
        return mock_module

    def mock_get_data(package, resource):
        return b'fake data'

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.pkgutil.get_data', mock_get_data)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_bytes', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=False)
    assert 'Collection.Util' in ps_module_dep_finder.ps_modules

def test_add_module_collection_util_not_found(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise ImportError

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=False)

def test_add_module_collection_util_optional(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise ImportError

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=True)
    assert 'Collection.Util' not in ps_module_dep_finder.ps_modules

def test_add_module_collection_util_multiple_paths(ps_module_dep_finder, monkeypatch):
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path/to/module', '/another/path']

    def mock_import_module(name):
        return mock_module

    def mock_get_data(package, resource):
        return b'fake data'

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.pkgutil.get_data', mock_get_data)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_bytes', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=False)

def test_add_module_collection_util_oserror(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise OSError(errno.ENOENT, "No such file or directory")

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=False)

def test_add_module_collection_util_oserror_optional(ps_module_dep_finder, monkeypatch):
    def mock_import_module(name):
        raise OSError(errno.ENOENT, "No such file or directory")

    monkeypatch.setattr('ansible.executor.powershell.module_manifest.import_module', mock_import_module)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_text', lambda x, errors=None: x)
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.to_native', lambda x, errors=None: x)

    ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'fqn', optional=True)
    assert 'Collection.Util' not in ps_module_dep_finder.ps_modules
