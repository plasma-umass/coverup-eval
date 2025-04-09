# file: semantic_release/dist.py:12-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}

import pytest

@pytest.fixture
def config(monkeypatch):
    config = {}
    monkeypatch.setattr('semantic_release.dist.config', config)
    return config

def test_should_build_with_build_command_and_upload_pypi(config):
    from semantic_release.dist import should_build
    config['build_command'] = 'build'
    config['upload_to_pypi'] = True
    config['upload_to_release'] = False
    assert should_build() is True

def test_should_build_with_build_command_and_upload_release(config):
    from semantic_release.dist import should_build
    config['build_command'] = 'build'
    config['upload_to_pypi'] = False
    config['upload_to_release'] = True
    assert should_build() is True

def test_should_build_with_build_command_and_no_upload(config):
    from semantic_release.dist import should_build
    config['build_command'] = 'build'
    config['upload_to_pypi'] = False
    config['upload_to_release'] = False
    assert should_build() is False

def test_should_build_with_no_build_command(config):
    from semantic_release.dist import should_build
    config['build_command'] = 'false'
    config['upload_to_pypi'] = True
    config['upload_to_release'] = True
    assert should_build() is False

def test_should_build_with_no_build_command_and_no_upload(config):
    from semantic_release.dist import should_build
    config['build_command'] = 'false'
    config['upload_to_pypi'] = False
    config['upload_to_release'] = False
    assert should_build() is False
