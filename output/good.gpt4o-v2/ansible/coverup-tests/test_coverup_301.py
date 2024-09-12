# file: lib/ansible/modules/debconf.py:113-126
# asked: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}
# gained: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}

import pytest

def test_get_selections_success(monkeypatch):
    class MockModule:
        def get_bin_path(self, arg, required):
            return "/usr/bin/debconf-show"
        
        def run_command(self, cmd):
            return (0, "key1: value1\nkey2: value2", "")

    module = MockModule()
    pkg = "dummy_package"
    
    from ansible.modules.debconf import get_selections
    selections = get_selections(module, pkg)
    
    assert selections == {
        "key1": "value1",
        "key2": "value2"
    }

def test_get_selections_failure(monkeypatch):
    class MockModule:
        def get_bin_path(self, arg, required):
            return "/usr/bin/debconf-show"
        
        def run_command(self, cmd):
            return (1, "", "error message")
        
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    module = MockModule()
    pkg = "dummy_package"
    
    from ansible.modules.debconf import get_selections
    
    with pytest.raises(Exception) as excinfo:
        get_selections(module, pkg)
    
    assert str(excinfo.value) == "error message"
