# file: semantic_release/dist.py:20-22
# asked: {"lines": [21, 22], "branches": []}
# gained: {"lines": [21, 22], "branches": []}

import pytest
from semantic_release.dist import should_remove_dist
from semantic_release.settings import config

@pytest.fixture
def mock_config(monkeypatch):
    mock_config_data = {
        "remove_dist": True,
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "build"
    }
    monkeypatch.setattr(config, "get", mock_config_data.get)
    return mock_config_data

def test_should_remove_dist(mock_config):
    assert should_remove_dist() is True

def test_should_not_remove_dist_when_remove_dist_is_false(monkeypatch):
    monkeypatch.setattr(config, "get", lambda key: False if key == "remove_dist" else None)
    assert should_remove_dist() is False

def test_should_not_remove_dist_when_should_not_build(monkeypatch):
    monkeypatch.setattr(config, "get", lambda key: True if key == "remove_dist" else None)
    monkeypatch.setattr(config, "get", lambda key: False if key == "build_command" else None)
    assert should_remove_dist() is False
