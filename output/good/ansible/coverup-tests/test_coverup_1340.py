# file lib/ansible/utils/collection_loader/_collection_finder.py:380-404
# lines [383, 384, 402]
# branches ['382->383', '394->398', '401->402']

import pytest
import sys
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockLoader(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        self._fullname = fullname
        self._redirect_module = None
        self._subpackage_search_paths = None
        self._parent_package_name = 'fake_parent'
        self._source_code_path = None

    def get_filename(self, fullname):
        return '/path/to/fake_module.py'

    def get_code(self, fullname):
        return compile("", "<string>", "exec")

    def _new_or_existing_module(self, fullname, **module_attrs):
        return super()._new_or_existing_module(fullname, **module_attrs)

@pytest.fixture
def mock_loader():
    loader = MockLoader('fake_module')
    return loader

def test_load_module_with_redirect_module(mock_loader, mocker):
    mock_loader._redirect_module = mocker.MagicMock()
    sys.modules['fake_module'] = None
    module = mock_loader.load_module('fake_module')
    assert sys.modules['fake_module'] is mock_loader._redirect_module
    assert module is mock_loader._redirect_module

def test_load_module_with_subpackage_search_paths(mock_loader, mocker):
    mock_loader._subpackage_search_paths = ['/path/to/fake_subpackage']
    module = mock_loader.load_module('fake_module')
    assert '__path__' in module.__dict__
    assert module.__dict__['__path__'] == ['/path/to/fake_subpackage']
    assert module.__dict__['__package__'] == 'fake_module'

def test_load_module_exec_code(mock_loader, mocker):
    mock_loader._subpackage_search_paths = None
    exec_mock = mocker.patch('builtins.exec')
    mock_loader.load_module('fake_module')
    exec_mock.assert_called_once()

@pytest.fixture(autouse=True)
def cleanup_sys_modules():
    yield
    sys.modules.pop('fake_module', None)
