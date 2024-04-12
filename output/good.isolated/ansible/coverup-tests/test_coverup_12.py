# file lib/ansible/executor/powershell/module_manifest.py:164-235
# lines [164, 165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 197, 198, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235]
# branches ['169->171', '169->184', '173->174', '173->180', '174->175', '174->177', '185->186', '185->194', '187->188', '187->192', '188->189', '188->190', '200->201', '200->203', '208->210', '208->212', '214->215', '214->222', '215->216', '215->218', '228->229', '228->231', '231->232', '231->234']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.plugins.loader import ps_module_utils_loader
from ansible.module_utils._text import to_bytes, to_native, to_text
import errno
import pkgutil
from importlib import import_module

# Mocking the necessary parts to test the PSModuleDepFinder class
@pytest.fixture
def ps_module_dep_finder(mocker):
    mocker.patch.object(ps_module_utils_loader, 'find_plugin', return_value=None)
    return PSModuleDepFinder()

def test_add_module_not_found_optional(mocker, ps_module_dep_finder):
    # Test the case where the module is not found and is optional
    mocker.patch.object(ps_module_utils_loader, 'find_plugin', return_value=None)
    ps_module_dep_finder._add_module("Ansible.Test", ".psm1", "fqn", optional=True)
    assert "Ansible.Test" not in ps_module_dep_finder.ps_modules

def test_add_module_not_found_not_optional(mocker, ps_module_dep_finder):
    # Test the case where the module is not found and is not optional
    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module("Ansible.Test", ".psm1", "fqn", optional=False)

def test_add_module_collection_import_error(mocker, ps_module_dep_finder):
    # Test the case where the collection module raises an ImportError
    mocker.patch('pkgutil.get_data', side_effect=ImportError("No package data found"))
    mocker.patch('importlib.import_module', return_value=mocker.Mock(__path__=['path']))
    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module("collection.Test", ".psm1", "collection.fqn", optional=False)

def test_add_module_collection_os_error(mocker, ps_module_dep_finder):
    # Test the case where the collection module raises an OSError
    mocker.patch('pkgutil.get_data', side_effect=OSError(errno.ENOENT, os.strerror(errno.ENOENT)))
    mocker.patch('importlib.import_module', return_value=mocker.Mock(__path__=['path']))
    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module("collection.Test", ".psm1", "collection.fqn", optional=False)

def test_add_module_collection_os_error_optional(mocker, ps_module_dep_finder):
    # Test the case where the collection module raises an OSError but is optional
    mocker.patch('pkgutil.get_data', side_effect=OSError(errno.ENOENT, os.strerror(errno.ENOENT)))
    mocker.patch('importlib.import_module', return_value=mocker.Mock(__path__=['path']))
    ps_module_dep_finder._add_module("collection.Test", ".psm1", "collection.fqn", optional=True)
    assert "collection.Test" not in ps_module_dep_finder.ps_modules

def test_add_module_collection_multiple_resource_paths(mocker, ps_module_dep_finder):
    # Test the case where the collection module has multiple resource paths
    mocker.patch('pkgutil.get_data', return_value=b'data')
    mocker.patch('importlib.import_module', return_value=mocker.Mock(__path__=['path1', 'path2']))
    with pytest.raises(AnsibleError):
        ps_module_dep_finder._add_module("collection.Test", ".psm1", "collection.fqn", optional=False)
