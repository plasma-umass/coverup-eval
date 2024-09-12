# file: lib/ansible/modules/apt_repository.py:310-346
# asked: {"lines": [310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 340, 341, 342, 344, 345, 346], "branches": [[311, 0], [311, 312], [312, 313], [312, 344], [317, 318], [317, 319], [322, 323], [322, 337], [324, 325], [324, 326], [327, 328], [327, 330], [340, 311], [340, 341], [345, 311], [345, 346]]}
# gained: {"lines": [310, 311, 312, 313, 314, 315, 319, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331, 333, 334, 337, 340, 341, 342, 344, 345, 346], "branches": [[311, 0], [311, 312], [312, 313], [312, 344], [322, 323], [322, 337], [324, 326], [327, 328], [340, 341], [345, 346]]}

import os
import tempfile
import pytest
from unittest import mock
from ansible.module_utils._text import to_native
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list():
    class MockModule:
        def fail_json(self, msg):
            raise Exception(msg)
        
        def atomic_move(self, src, dest):
            os.rename(src, dest)
        
        def set_mode_if_different(self, path, mode, diff):
            os.chmod(path, mode)
        
        @property
        def params(self):
            return {'mode': 0o644}
    
    module = MockModule()
    
    with mock.patch('ansible.modules.apt_repository.apt_pkg'):
        sl = SourcesList(module)
    
    sl.files = {}
    sl.new_repos = []
    return sl

def test_save_creates_directory_and_file(sources_list):
    sources_list.files = {
        '/tmp/test_sources.list': [(1, True, True, 'deb http://example.com stable main', 'example comment')]
    }
    sources_list.new_repos = ['/tmp/test_sources.list']
    
    with mock.patch('os.makedirs') as makedirs_mock, \
         mock.patch('tempfile.mkstemp', return_value=(1, '/tmp/.test_sources.list-XXXXXX')) as mkstemp_mock, \
         mock.patch('os.fdopen', mock.mock_open()) as fdopen_mock, \
         mock.patch('os.path.isdir', return_value=True), \
         mock.patch('os.rename'), \
         mock.patch('os.chmod'):
        
        sources_list.save()
        
        makedirs_mock.assert_called_once_with('/tmp')
        mkstemp_mock.assert_called_once_with(prefix='.test_sources.list-', dir='/tmp')
        fdopen_mock.assert_called_once_with(1, 'w')
        fdopen_mock().write.assert_called_once_with('deb http://example.com stable main # example comment\n')

def test_save_removes_empty_file(sources_list):
    sources_list.files = {
        '/tmp/test_sources.list': []
    }
    
    with mock.patch('os.path.exists', return_value=True) as exists_mock, \
         mock.patch('os.remove') as remove_mock:
        
        sources_list.save()
        
        exists_mock.assert_called_once_with('/tmp/test_sources.list')
        remove_mock.assert_called_once_with('/tmp/test_sources.list')
