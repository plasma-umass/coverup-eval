# file: lib/ansible/module_utils/facts/packages.py:72-86
# asked: {"lines": [78, 79, 82, 83, 84, 85, 86], "branches": []}
# gained: {"lines": [78, 79, 82, 83, 84, 85, 86], "branches": []}

import pytest
from ansible.module_utils.facts.packages import CLIMgr
from ansible.module_utils.basic import get_bin_path

class TestCLIMgr:
    
    @pytest.fixture(autouse=True)
    def setup_method(self, monkeypatch):
        class TestCLIMgrConcrete(CLIMgr):
            def get_package_details(self, package_name):
                pass
            
            def list_installed(self):
                pass
        
        self.cli_mgr = TestCLIMgrConcrete()
        monkeypatch.setattr(self.cli_mgr, 'CLI', 'fakecli')
    
    def test_init(self):
        assert self.cli_mgr._cli is None
    
    def test_is_available_success(self, monkeypatch):
        def mock_get_bin_path(cli):
            return '/usr/bin/fakecli'
        
        monkeypatch.setattr('ansible.module_utils.facts.packages.get_bin_path', mock_get_bin_path)
        assert self.cli_mgr.is_available() is True
        assert self.cli_mgr._cli == '/usr/bin/fakecli'
    
    def test_is_available_failure(self, monkeypatch):
        def mock_get_bin_path(cli):
            raise ValueError("CLI not found")
        
        monkeypatch.setattr('ansible.module_utils.facts.packages.get_bin_path', mock_get_bin_path)
        assert self.cli_mgr.is_available() is False
        assert self.cli_mgr._cli is None
