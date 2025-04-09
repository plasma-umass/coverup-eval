# file: semantic_release/dist.py:20-22
# asked: {"lines": [20, 21, 22], "branches": []}
# gained: {"lines": [20, 21, 22], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the function should_remove_dist is imported from semantic_release.dist
from semantic_release.dist import should_remove_dist

@pytest.fixture
def mock_config(monkeypatch):
    config = {"remove_dist": True}
    monkeypatch.setattr('semantic_release.dist.config', config)
    return config

@pytest.fixture
def mock_should_build(monkeypatch):
    monkeypatch.setattr('semantic_release.dist.should_build', lambda: True)

def test_should_remove_dist_true(mock_config, mock_should_build):
    assert should_remove_dist() is True

def test_should_remove_dist_false_no_remove_dist(monkeypatch, mock_should_build):
    monkeypatch.setattr('semantic_release.dist.config', {"remove_dist": False})
    assert should_remove_dist() is False

def test_should_remove_dist_false_no_should_build(monkeypatch):
    monkeypatch.setattr('semantic_release.dist.config', {"remove_dist": True})
    monkeypatch.setattr('semantic_release.dist.should_build', lambda: False)
    assert should_remove_dist() is False
