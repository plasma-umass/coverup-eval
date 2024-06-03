# file lib/ansible/module_utils/facts/packages.py:53-69
# lines [53, 55, 57, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.facts.packages import LibMgr

class TestLibMgr:
    
    @pytest.fixture
    def lib_mgr(self):
        class TestLibMgr(LibMgr):
            LIB = 'testlib'
            def get_package_details(self):
                pass
            def list_installed(self):
                pass
        return TestLibMgr()

    def test_is_available_success(self, lib_mgr, mocker):
        mocker.patch('builtins.__import__', return_value=mock.Mock())
        assert lib_mgr.is_available() is True
        assert lib_mgr._lib is not None

    def test_is_available_failure(self, lib_mgr, mocker):
        mocker.patch('builtins.__import__', side_effect=ImportError)
        assert lib_mgr.is_available() is False
        assert lib_mgr._lib is None
