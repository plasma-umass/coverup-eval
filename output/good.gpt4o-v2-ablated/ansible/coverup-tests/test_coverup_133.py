# file: lib/ansible/cli/arguments/option_helpers.py:90-100
# asked: {"lines": [90, 92, 93, 94, 96, 97, 99, 100], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}
# gained: {"lines": [90, 92, 93, 94, 96, 97, 99, 100], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}

import pytest
import os
from ansible.cli.arguments.option_helpers import unfrack_path

def test_unfrack_path_single_path(monkeypatch):
    def mock_unfrackpath(value):
        return f"unfracked_{value}"
    
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrackpath', mock_unfrackpath)
    
    path_func = unfrack_path()
    result = path_func("some/path")
    assert result == "unfracked_some/path"

def test_unfrack_path_dash_value(monkeypatch):
    def mock_unfrackpath(value):
        return f"unfracked_{value}"
    
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrackpath', mock_unfrackpath)
    
    path_func = unfrack_path()
    result = path_func("-")
    assert result == "-"

def test_unfrack_path_with_pathsep(monkeypatch):
    def mock_unfrackpath(value):
        return f"unfracked_{value}"
    
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrackpath', mock_unfrackpath)
    
    path_func = unfrack_path(pathsep=True)
    result = path_func(f"some{os.pathsep}path{os.pathsep}values")
    assert result == ["unfracked_some", "unfracked_path", "unfracked_values"]

def test_unfrack_path_with_empty_pathsep(monkeypatch):
    def mock_unfrackpath(value):
        return f"unfracked_{value}"
    
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrackpath', mock_unfrackpath)
    
    path_func = unfrack_path(pathsep=True)
    result = path_func(f"some{os.pathsep}{os.pathsep}path")
    assert result == ["unfracked_some", "unfracked_path"]
