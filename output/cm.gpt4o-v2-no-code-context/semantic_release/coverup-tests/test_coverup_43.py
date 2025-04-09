# file: semantic_release/dist.py:12-17
# asked: {"lines": [13, 14, 15, 16, 17], "branches": []}
# gained: {"lines": [13, 14, 15, 16, 17], "branches": []}

import pytest

def test_should_build_with_upload_pypi_and_build_command(monkeypatch):
    config = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "build"
    }
    monkeypatch.setattr('semantic_release.dist.config', config)
    from semantic_release.dist import should_build
    assert should_build() is True

def test_should_build_with_upload_release_and_build_command(monkeypatch):
    config = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "build"
    }
    monkeypatch.setattr('semantic_release.dist.config', config)
    from semantic_release.dist import should_build
    assert should_build() is True

def test_should_build_with_no_upload_and_build_command(monkeypatch):
    config = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "build"
    }
    monkeypatch.setattr('semantic_release.dist.config', config)
    from semantic_release.dist import should_build
    assert should_build() is False

def test_should_build_with_upload_pypi_and_no_build_command(monkeypatch):
    config = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "false"
    }
    monkeypatch.setattr('semantic_release.dist.config', config)
    from semantic_release.dist import should_build
    assert should_build() is False

def test_should_build_with_upload_release_and_no_build_command(monkeypatch):
    config = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "false"
    }
    monkeypatch.setattr('semantic_release.dist.config', config)
    from semantic_release.dist import should_build
    assert should_build() is False
