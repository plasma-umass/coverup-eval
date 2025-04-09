# file: lib/ansible/module_utils/common/validation.py:530-535
# asked: {"lines": [530, 534, 535], "branches": []}
# gained: {"lines": [530, 534, 535], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_path

def test_check_type_path_with_string(monkeypatch):
    def mock_expanduser(path):
        return path.replace("~", "/home/user")
    
    def mock_expandvars(path):
        return path.replace("$VAR", "value")
    
    monkeypatch.setattr("os.path.expanduser", mock_expanduser)
    monkeypatch.setattr("os.path.expandvars", mock_expandvars)
    
    result = check_type_path("~/path/to/$VAR")
    assert result == "/home/user/path/to/value"

def test_check_type_path_with_non_string(monkeypatch):
    def mock_expanduser(path):
        return path.replace("~", "/home/user")
    
    def mock_expandvars(path):
        return path.replace("$VAR", "value")
    
    monkeypatch.setattr("os.path.expanduser", mock_expanduser)
    monkeypatch.setattr("os.path.expandvars", mock_expandvars)
    
    result = check_type_path(12345)
    assert result == "12345"
