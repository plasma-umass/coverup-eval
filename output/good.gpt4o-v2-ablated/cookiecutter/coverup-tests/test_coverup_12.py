# file: cookiecutter/find.py:10-31
# asked: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}
# gained: {"lines": [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31], "branches": [[21, 22], [21, 26], [22, 21], [22, 23], [26, 27], [26, 31]]}

import os
import pytest
from unittest import mock

# Assuming the find_template function is imported from cookiecutter.find
from cookiecutter.find import find_template, NonTemplatedInputDirException

def test_find_template_success(monkeypatch):
    repo_dir = '/fake/repo/dir'
    repo_dir_contents = ['cookiecutter-{{project_name}}']

    def mock_listdir(path):
        assert path == repo_dir
        return repo_dir_contents

    monkeypatch.setattr(os, 'listdir', mock_listdir)

    result = find_template(repo_dir)
    assert result == os.path.join(repo_dir, 'cookiecutter-{{project_name}}')

def test_find_template_no_template(monkeypatch):
    repo_dir = '/fake/repo/dir'
    repo_dir_contents = ['not_a_template']

    def mock_listdir(path):
        assert path == repo_dir
        return repo_dir_contents

    monkeypatch.setattr(os, 'listdir', mock_listdir)

    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)

def test_find_template_multiple_items(monkeypatch):
    repo_dir = '/fake/repo/dir'
    repo_dir_contents = ['not_a_template', 'cookiecutter-{{project_name}}']

    def mock_listdir(path):
        assert path == repo_dir
        return repo_dir_contents

    monkeypatch.setattr(os, 'listdir', mock_listdir)

    result = find_template(repo_dir)
    assert result == os.path.join(repo_dir, 'cookiecutter-{{project_name}}')
