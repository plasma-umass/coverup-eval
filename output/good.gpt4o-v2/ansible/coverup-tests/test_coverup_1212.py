# file: lib/ansible/module_utils/facts/packages.py:53-69
# asked: {"lines": [59, 60, 63, 64, 65, 66, 67, 68, 69], "branches": []}
# gained: {"lines": [59, 60, 63, 64, 65, 66, 67, 68, 69], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the LibMgr class is defined in ansible.module_utils.facts.packages
from ansible.module_utils.facts.packages import LibMgr

class TestLibMgr:
    
    @patch('builtins.__import__')
    def test_is_available_success(self, mock_import):
        class TestLib(LibMgr):
            LIB = 'testlib'
            
            def get_package_details(self, package):
                pass
            
            def list_installed(self):
                pass
        
        mock_import.return_value = MagicMock()
        lib_mgr = TestLib()
        
        assert lib_mgr.is_available() is True
        mock_import.assert_called_once_with('testlib')
        assert lib_mgr._lib is not None

    @patch('builtins.__import__')
    def test_is_available_failure(self, mock_import):
        class TestLib(LibMgr):
            LIB = 'testlib'
            
            def get_package_details(self, package):
                pass
            
            def list_installed(self):
                pass
        
        mock_import.side_effect = ImportError
        lib_mgr = TestLib()
        
        assert lib_mgr.is_available() is False
        mock_import.assert_called_once_with('testlib')
        assert lib_mgr._lib is None
