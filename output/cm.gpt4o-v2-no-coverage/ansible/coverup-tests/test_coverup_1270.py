# file: lib/ansible/cli/arguments/option_helpers.py:90-100
# asked: {"lines": [93, 94, 96, 97, 99], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}
# gained: {"lines": [93, 94, 96, 97, 99], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}

import os
import pytest
from ansible.utils.path import unfrackpath
from ansible.cli.arguments.option_helpers import unfrack_path

def test_unfrack_path_no_pathsep(monkeypatch):
    def mock_unfrackpath(value, follow=True, basedir=None):
        return f"/output/{value}"
    
    monkeypatch.setattr('ansible.utils.path.unfrackpath', mock_unfrackpath)
    
    inner = unfrack_path(pathsep=False)
    
    # Test with value '-'
    result = inner('-')
    assert result == '-'
    
    # Test with a normal path
    result = inner('some/path')
    assert result == '/output/some/path'

def test_unfrack_path_with_pathsep(monkeypatch):
    def mock_unfrackpath(value, follow=True, basedir=None):
        return f"/output/{value}"
    
    monkeypatch.setattr('ansible.utils.path.unfrackpath', mock_unfrackpath)
    
    inner = unfrack_path(pathsep=True)
    
    # Test with multiple paths separated by os.pathsep
    value = f"some/path{os.pathsep}another/path"
    result = inner(value)
    expected = ["/output/some/path", "/output/another/path"]
    assert result == expected
    
    # Test with empty paths
    value = f"some/path{os.pathsep}{os.pathsep}another/path"
    result = inner(value)
    expected = ["/output/some/path", "/output/another/path"]
    assert result == expected
