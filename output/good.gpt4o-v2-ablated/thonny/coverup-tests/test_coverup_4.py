# file: thonny/jedi_utils.py:90-96
# asked: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}
# gained: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}

import pytest
import jedi
from thonny.jedi_utils import _get_new_jedi_project

def test_get_new_jedi_project_with_empty_sys_path():
    assert _get_new_jedi_project([]) is None

def test_get_new_jedi_project_with_valid_sys_path(monkeypatch):
    class MockProject:
        def __init__(self, path, added_sys_path):
            self.path = path
            self.added_sys_path = added_sys_path

    def mock_project(path, added_sys_path):
        return MockProject(path, added_sys_path)

    monkeypatch.setattr(jedi, 'Project', mock_project)
    
    sys_path = ['/some/path']
    project = _get_new_jedi_project(sys_path)
    
    assert project is not None
    assert project.path == sys_path[0]
    assert project.added_sys_path == sys_path
