# file: cookiecutter/find.py:10-31
# asked: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}
# gained: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}

import os
import pytest
from cookiecutter.find import find_template
from cookiecutter.exceptions import NonTemplatedInputDirException

def test_find_template_success(monkeypatch):
    repo_dir = 'test_repo'
    template_dir = 'cookiecutter_project{{cookiecutter.repo_name}}'
    
    def mock_listdir(path):
        return [template_dir]
    
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    
    result = find_template(repo_dir)
    expected = os.path.join(repo_dir, template_dir)
    
    assert result == expected

def test_find_template_failure(monkeypatch):
    repo_dir = 'test_repo'
    
    def mock_listdir(path):
        return ['some_other_dir']
    
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    
    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)
