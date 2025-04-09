# file lib/ansible/executor/powershell/module_manifest.py:164-235
# lines [165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 197, 198, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235]
# branches ['169->171', '169->184', '173->174', '173->180', '174->175', '174->177', '185->186', '185->194', '187->188', '187->192', '188->189', '188->190', '200->201', '200->203', '208->210', '208->212', '214->215', '214->222', '215->216', '215->218', '228->229', '228->231', '231->232', '231->234']

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder, AnsibleError, to_text, to_bytes, _slurp
import os
import errno
import pkgutil
from importlib import import_module

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder.ps_modules = {}
    finder.cs_utils_wrapper = {}
    finder.cs_utils_module = {}
    return finder

@patch('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin')
@patch('ansible.executor.powershell.module_manifest._slurp')
@patch('ansible.executor.powershell.module_manifest.import_module')
@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
def test_add_module_builtin_util(mock_get_data, mock_import_module, mock_slurp, mock_find_plugin, ps_module_dep_finder):
    mock_find_plugin.return_value = 'mock_path'
    mock_slurp.return_value = b'module data'
    
    ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'Ansible.Builtin', optional=False)
    
    assert 'Ansible.Builtin' in ps_module_dep_finder.ps_modules
    assert ps_module_dep_finder.ps_modules['Ansible.Builtin']['data'] == b'module data'
    assert ps_module_dep_finder.ps_modules['Ansible.Builtin']['path'] == 'mock_path'

@patch('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin')
@patch('ansible.executor.powershell.module_manifest._slurp')
@patch('ansible.executor.powershell.module_manifest.import_module')
@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
def test_add_module_collection_util(mock_get_data, mock_import_module, mock_slurp, mock_find_plugin, ps_module_dep_finder):
    mock_import_module.return_value.__path__ = ['mock_path']
    mock_get_data.return_value = b'collection data'
    
    ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'Collection.Util', optional=False)
    
    assert 'Collection.Util' in ps_module_dep_finder.ps_modules
    assert ps_module_dep_finder.ps_modules['Collection.Util']['data'] == b'collection data'
    assert ps_module_dep_finder.ps_modules['Collection.Util']['path'] == 'mock_path/Util.psm1'

@patch('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin')
@patch('ansible.executor.powershell.module_manifest._slurp')
@patch('ansible.executor.powershell.module_manifest.import_module')
@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
def test_add_module_optional_not_found(mock_get_data, mock_import_module, mock_slurp, mock_find_plugin, ps_module_dep_finder):
    mock_find_plugin.return_value = None
    
    ps_module_dep_finder._add_module('Ansible.Optional', '.psm1', 'Ansible.Optional', optional=True)
    
    assert 'Ansible.Optional' not in ps_module_dep_finder.ps_modules

@patch('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin')
@patch('ansible.executor.powershell.module_manifest._slurp')
@patch('ansible.executor.powershell.module_manifest.import_module')
@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
def test_add_module_import_error(mock_get_data, mock_import_module, mock_slurp, mock_find_plugin, ps_module_dep_finder):
    mock_import_module.side_effect = ImportError
    
    with pytest.raises(AnsibleError, match='Could not find collection imported module support code for'):
        ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'Collection.Util', optional=False)
    
    assert 'Collection.Util' not in ps_module_dep_finder.ps_modules

@patch('ansible.executor.powershell.module_manifest.ps_module_utils_loader.find_plugin')
@patch('ansible.executor.powershell.module_manifest._slurp')
@patch('ansible.executor.powershell.module_manifest.import_module')
@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
def test_add_module_os_error(mock_get_data, mock_import_module, mock_slurp, mock_find_plugin, ps_module_dep_finder):
    mock_import_module.side_effect = OSError(errno.ENOENT, 'No such file or directory')
    
    with pytest.raises(AnsibleError, match='Could not find collection imported module support code for'):
        ps_module_dep_finder._add_module('Collection.Util', '.psm1', 'Collection.Util', optional=False)
    
    assert 'Collection.Util' not in ps_module_dep_finder.ps_modules
