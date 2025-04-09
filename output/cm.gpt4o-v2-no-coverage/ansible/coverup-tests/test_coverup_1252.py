# file: lib/ansible/executor/powershell/module_manifest.py:164-235
# asked: {"lines": [165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 197, 198, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 213, 214, 215, 216, 218, 219, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 175], [174, 177], [185, 186], [185, 194], [187, 188], [187, 192], [188, 189], [188, 190], [200, 201], [200, 203], [208, 210], [208, 212], [214, 215], [214, 222], [215, 216], [215, 218], [228, 229], [228, 231], [231, 232], [231, 234]]}
# gained: {"lines": [165, 167, 169, 171, 173, 174, 175, 177, 178, 180, 184, 185, 194, 195, 197, 198, 199, 200, 203, 204, 207, 208, 212, 213, 214, 215, 216, 218, 219, 224, 225, 226, 228, 229, 231, 234, 235], "branches": [[169, 171], [169, 184], [173, 174], [173, 180], [174, 175], [174, 177], [185, 194], [200, 203], [208, 212], [214, 215], [215, 216], [215, 218], [228, 229], [228, 231], [231, 234]]}

import pytest
import errno
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_add_module_builtin_util(ps_module_dep_finder):
    with patch('ansible.plugins.loader.ps_module_utils_loader.find_plugin', return_value='/fake/path'), \
         patch('ansible.executor.powershell.module_manifest._slurp', return_value=b'fake data'), \
         patch('ansible.executor.powershell.module_manifest.to_bytes', return_value=b'fake data'), \
         patch.object(ps_module_dep_finder, 'scan_module') as mock_scan_module:
        
        ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'fqn', False)
        
        assert 'Ansible.Builtin' in ps_module_dep_finder.ps_modules
        mock_scan_module.assert_called_once()

def test_add_module_builtin_util_not_found(ps_module_dep_finder):
    with patch('ansible.plugins.loader.ps_module_utils_loader.find_plugin', return_value=None):
        with pytest.raises(AnsibleError, match="Could not find imported module support code for 'Ansible.Builtin'"):
            ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'fqn', False)

def test_add_module_collection_util(ps_module_dep_finder):
    with patch('ansible.executor.powershell.module_manifest.import_module', return_value=MagicMock(__path__=['/fake/path'])), \
         patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b'fake data'), \
         patch('ansible.executor.powershell.module_manifest.to_bytes', return_value=b'fake data'), \
         patch.object(ps_module_dep_finder, 'scan_module') as mock_scan_module:
        
        ps_module_dep_finder._add_module('ansible_collections.test.module', '.py', 'fqn', False)
        
        assert 'ansible_collections.test.module' in ps_module_dep_finder.cs_utils_module
        mock_scan_module.assert_called_once()

def test_add_module_collection_util_not_found(ps_module_dep_finder):
    with patch('ansible.executor.powershell.module_manifest.import_module', side_effect=ImportError):
        with pytest.raises(AnsibleError, match="Could not find collection imported module support code for 'ansible_collections.test.module'"):
            ps_module_dep_finder._add_module('ansible_collections.test.module', '.py', 'fqn', False)

def test_add_module_optional_not_found(ps_module_dep_finder):
    with patch('ansible.plugins.loader.ps_module_utils_loader.find_plugin', return_value=None):
        ps_module_dep_finder._add_module('Ansible.Builtin', '.psm1', 'fqn', True)
        assert 'Ansible.Builtin' not in ps_module_dep_finder.ps_modules

def test_add_module_collection_util_oserror(ps_module_dep_finder):
    with patch('ansible.executor.powershell.module_manifest.import_module', side_effect=OSError(errno.ENOENT, 'No such file or directory')):
        ps_module_dep_finder._add_module('ansible_collections.test.module', '.py', 'fqn', True)
        assert 'ansible_collections.test.module' not in ps_module_dep_finder.cs_utils_module
