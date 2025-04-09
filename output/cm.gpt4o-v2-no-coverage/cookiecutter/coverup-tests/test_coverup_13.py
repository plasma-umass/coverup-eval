# file: cookiecutter/find.py:10-31
# asked: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}
# gained: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}

import os
import pytest
from cookiecutter.find import find_template
from cookiecutter.exceptions import NonTemplatedInputDirException

def test_find_template_success(monkeypatch, tmp_path):
    # Setup
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    template_dir = repo_dir / "cookiecutter-project-{{cookiecutter.project_name}}"
    template_dir.mkdir()
    
    # Mock os.listdir to return the contents of the repo_dir
    monkeypatch.setattr(os, 'listdir', lambda x: [template_dir.name] if x == str(repo_dir) else os.listdir(x))
    
    # Execute
    result = find_template(str(repo_dir))
    
    # Verify
    assert result == str(template_dir)

def test_find_template_failure(monkeypatch, tmp_path):
    # Setup
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    non_template_dir = repo_dir / "non-template-dir"
    non_template_dir.mkdir()
    
    # Mock os.listdir to return the contents of the repo_dir
    monkeypatch.setattr(os, 'listdir', lambda x: [non_template_dir.name] if x == str(repo_dir) else os.listdir(x))
    
    # Execute and Verify
    with pytest.raises(NonTemplatedInputDirException):
        find_template(str(repo_dir))
