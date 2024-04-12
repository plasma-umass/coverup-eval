# file lib/ansible/executor/powershell/module_manifest.py:164-235
# lines [180, 186, 187, 188, 189, 190, 192, 199, 200, 201, 203, 204, 207, 208, 210, 211, 212, 222, 224, 225, 226, 228, 229, 231, 232, 234, 235]
# branches ['173->180', '185->186', '187->188', '187->192', '188->189', '188->190', '200->201', '200->203', '208->210', '208->212', '214->222', '228->229', '228->231', '231->232', '231->234']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_bytes, to_text, to_native
from ansible.plugins.loader import ps_module_utils_loader
from unittest.mock import MagicMock, patch

# Define a test class to encapsulate the tests
class TestPSModuleDepFinder:

    # Test function to cover missing lines
    @pytest.fixture
    def ps_module_dep_finder(self):
        return PSModuleDepFinder()

    @pytest.fixture
    def cleanup(self, mocker):
        # Cleanup code to ensure no side effects for other tests
        mocker.patch.object(ps_module_utils_loader, 'find_plugin', return_value=None)

    def test_add_module_builtin_util_not_found(self, ps_module_dep_finder, cleanup):
        with pytest.raises(AnsibleError):
            ps_module_dep_finder._add_module("Ansible.NonExistentUtil", ".psm1", "fqn", False)

    def test_add_module_collection_util_not_found(self, ps_module_dep_finder, cleanup):
        with pytest.raises(AnsibleError):
            ps_module_dep_finder._add_module("NonExistent.Collection.Util", ".psm1", "fqn", False)

    def test_add_module_collection_util_optional_not_found(self, ps_module_dep_finder, cleanup):
        # Optional util should not raise an exception
        ps_module_dep_finder._add_module("NonExistent.Collection.Util", ".psm1", "fqn", True)

    def test_add_module_collection_util_with_relative_import(self, ps_module_dep_finder, cleanup, mocker):
        mocker.patch('ansible.executor.powershell.module_manifest.import_module', return_value=MagicMock(__path__=['/path/to/module']))
        mocker.patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b'data')
        ps_module_dep_finder._add_module(".Util", ".psm1", "Collection.Module", False)
        assert "Collection.Module.Util" in ps_module_dep_finder.ps_modules or ".Util" in ps_module_dep_finder.ps_modules

    def test_add_module_collection_util_with_multiple_paths(self, ps_module_dep_finder, cleanup, mocker):
        mocker.patch('ansible.executor.powershell.module_manifest.import_module', return_value=MagicMock(__path__=['/path/one', '/path/two']))
        with pytest.raises(AnsibleError):
            ps_module_dep_finder._add_module("Collection.Module.Util", ".psm1", "fqn", False)

    def test_add_module_collection_util_with_wrapper(self, ps_module_dep_finder, cleanup, mocker):
        mocker.patch('ansible.executor.powershell.module_manifest.import_module', return_value=MagicMock(__path__=['/path/to/module']))
        mocker.patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b'data')
        ps_module_dep_finder._add_module("Collection.Module.Util", ".dll", "fqn", False, wrapper=True)
        assert "Collection.Module.Util" in ps_module_dep_finder.cs_utils_wrapper

    def test_add_module_collection_util_without_wrapper(self, ps_module_dep_finder, cleanup, mocker):
        mocker.patch('ansible.executor.powershell.module_manifest.import_module', return_value=MagicMock(__path__=['/path/to/module']))
        mocker.patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=b'data')
        ps_module_dep_finder._add_module("Collection.Module.Util", ".dll", "fqn", False, wrapper=False)
        assert "Collection.Module.Util" in ps_module_dep_finder.cs_utils_module
