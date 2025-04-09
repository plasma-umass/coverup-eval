# file: lib/ansible/playbook/base.py:858-869
# asked: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}
# gained: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the Base class is imported from ansible.playbook.base
from ansible.playbook.base import Base

class TestBase:
    
    @pytest.fixture
    def base_instance(self):
        return Base()

    def test_get_path_direct(self, base_instance):
        base_instance._ds = Mock()
        base_instance._ds._data_source = "source"
        base_instance._ds._line_number = 42
        
        path = base_instance.get_path()
        
        assert path == "source:42"

    def test_get_path_parent(self, base_instance):
        base_instance._ds = None
        base_instance._parent = Mock()
        base_instance._parent._play._ds._data_source = "parent_source"
        base_instance._parent._play._ds._line_number = 84
        
        path = base_instance.get_path()
        
        assert path == "parent_source:84"

    def test_get_path_no_path(self, base_instance):
        base_instance._ds = None
        base_instance._parent = None
        
        path = base_instance.get_path()
        
        assert path == ""
