# file: thonny/jedi_utils.py:90-96
# asked: {"lines": [91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}
# gained: {"lines": [91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}

import pytest
from thonny.jedi_utils import _get_new_jedi_project
import jedi

def test_get_new_jedi_project_with_empty_sys_path():
    result = _get_new_jedi_project([])
    assert result is None

def test_get_new_jedi_project_with_valid_sys_path(monkeypatch):
    class MockProject:
        def __init__(self, path, added_sys_path):
            self.path = path
            self.added_sys_path = added_sys_path

    def mock_jedi_project(path, added_sys_path):
        return MockProject(path, added_sys_path)

    monkeypatch.setattr(jedi, 'Project', mock_jedi_project)
    
    sys_path = ['/some/path']
    result = _get_new_jedi_project(sys_path)
    
    assert isinstance(result, MockProject)
    assert result.path == sys_path[0]
    assert result.added_sys_path == sys_path
