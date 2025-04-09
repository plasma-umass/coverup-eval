# file: flutils/pathutils.py:504-560
# asked: {"lines": [554], "branches": [[553, 554]]}
# gained: {"lines": [554], "branches": [[553, 554]]}

import os
import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_absolute_path(monkeypatch):
    # Ensure the path is absolute
    path = "/tmp/foo/bar"
    result = normalize_path(path)
    assert result == Path(path)

def test_normalize_path_relative_path(monkeypatch):
    # Ensure the path is relative
    relative_path = "foo/bar"
    current_working_directory = "/home/test_user"
    
    # Mock os.getcwd to return a specific directory
    monkeypatch.setattr(os, "getcwd", lambda: current_working_directory)
    
    result = normalize_path(relative_path)
    expected_path = os.path.join(current_working_directory, relative_path)
    assert result == Path(expected_path)

def test_normalize_path_with_env_variable(monkeypatch):
    # Ensure the path contains an environment variable
    env_var = "TEST_ENV_VAR"
    env_value = "/env/path"
    monkeypatch.setenv(env_var, env_value)
    
    path_with_env = f"${env_var}/foo/bar"
    result = normalize_path(path_with_env)
    expected_path = os.path.join(env_value, "foo/bar")
    assert result == Path(expected_path)

def test_normalize_path_with_user_home(monkeypatch):
    # Ensure the path contains a user home directory
    user_home = "/home/test_user"
    monkeypatch.setattr(os.path, "expanduser", lambda x: x.replace("~", user_home))
    
    path_with_home = "~/foo/bar"
    result = normalize_path(path_with_home)
    expected_path = os.path.join(user_home, "foo/bar")
    assert result == Path(expected_path)
