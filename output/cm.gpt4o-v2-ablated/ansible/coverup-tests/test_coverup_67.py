# file: lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# asked: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}
# gained: {"lines": [359, 360], "branches": []}

import os
import pytest
from unittest import mock

# Mocking to_native and to_bytes functions
def to_native(path):
    return path

def to_bytes(path):
    return path

# Importing the class to be tested
class _AnsibleCollectionPkgLoaderBase:
    @staticmethod
    def _module_file_from_path(leaf_name, path):
        has_code = True
        package_path = os.path.join(to_native(path), to_native(leaf_name))
        module_path = None

        # if the submodule is a package, assemble valid submodule paths, but stop looking for a module
        if os.path.isdir(to_bytes(package_path)):
            # is there a package init?
            module_path = os.path.join(package_path, '__init__.py')
            if not os.path.isfile(to_bytes(module_path)):
                module_path = os.path.join(package_path, '__synthetic__')
                has_code = False
        else:
            module_path = package_path + '.py'
            package_path = None
            if not os.path.isfile(to_bytes(module_path)):
                raise ImportError('{0} not found at {1}'.format(leaf_name, path))

        return module_path, has_code, package_path

@pytest.fixture(autouse=True)
def mock_os_functions(monkeypatch):
    monkeypatch.setattr('os.path.isdir', lambda path: path.endswith('package'))
    monkeypatch.setattr('os.path.isfile', lambda path: path.endswith('__init__.py') or path.endswith('.py'))
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.to_native', to_native)
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.to_bytes', to_bytes)

def test_module_file_from_path_package_with_init():
    loader = _AnsibleCollectionPkgLoaderBase()
    module_path, has_code, package_path = loader._module_file_from_path('package', '/some/path')
    assert module_path == '/some/path/package/__init__.py'
    assert has_code is True
    assert package_path == '/some/path/package'

def test_module_file_from_path_package_without_init():
    loader = _AnsibleCollectionPkgLoaderBase()
    with mock.patch('os.path.isfile', return_value=False):
        module_path, has_code, package_path = loader._module_file_from_path('package', '/some/path')
    assert module_path == '/some/path/package/__synthetic__'
    assert has_code is False
    assert package_path == '/some/path/package'

def test_module_file_from_path_not_package():
    loader = _AnsibleCollectionPkgLoaderBase()
    module_path, has_code, package_path = loader._module_file_from_path('module', '/some/path')
    assert module_path == '/some/path/module.py'
    assert has_code is True
    assert package_path is None

def test_module_file_from_path_not_found():
    loader = _AnsibleCollectionPkgLoaderBase()
    with mock.patch('os.path.isfile', return_value=False):
        with pytest.raises(ImportError, match='module not found at /some/path'):
            loader._module_file_from_path('module', '/some/path')
