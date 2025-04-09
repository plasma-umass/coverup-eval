# file: lib/ansible/module_utils/facts/packages.py:53-69
# asked: {"lines": [59, 60, 63, 64, 65, 66, 67, 68, 69], "branches": []}
# gained: {"lines": [59, 60, 63, 64, 65, 66, 67, 68, 69], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the code above is in a module named 'packages'
from ansible.module_utils.facts.packages import LibMgr

class TestLibMgr:
    
    @pytest.fixture
    def lib_mgr(self):
        class TestLibMgr(LibMgr):
            LIB = 'fake_lib'
            def get_package_details(self):
                pass
            def list_installed(self):
                pass
        return TestLibMgr()

    def test_init(self, lib_mgr):
        assert lib_mgr._lib is None

    def test_is_available_success(self, lib_mgr, monkeypatch):
        fake_lib = MagicMock()
        monkeypatch.setattr('builtins.__import__', lambda name: fake_lib if name == 'fake_lib' else None)
        
        assert lib_mgr.is_available() is True
        assert lib_mgr._lib is fake_lib

    def test_is_available_failure(self, lib_mgr, monkeypatch):
        def mock_import(name):
            if name == 'fake_lib':
                raise ImportError
            return None
        
        monkeypatch.setattr('builtins.__import__', mock_import)
        
        assert lib_mgr.is_available() is False
        assert lib_mgr._lib is None
