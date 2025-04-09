# file sanic/blueprint_group.py:164-180
# lines [164, 172, 173, 174, 175, 176, 177, 178, 179, 180]
# branches ['172->173', '172->177', '177->178', '177->180', '178->177', '178->179']

import pytest
from sanic import Blueprint
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup(url_prefix='/group', version=1, strict_slashes=True)

@pytest.fixture
def blueprint():
    return Blueprint('test', url_prefix='/test')

def test_sanitize_blueprint(blueprint_group, blueprint):
    sanitized_bp = blueprint_group._sanitize_blueprint(blueprint)
    assert sanitized_bp.url_prefix == '/group/test'
    assert sanitized_bp.version == 1
    assert sanitized_bp.strict_slashes is True

def test_sanitize_blueprint_no_url_prefix(blueprint_group, blueprint):
    blueprint_group._url_prefix = None
    sanitized_bp = blueprint_group._sanitize_blueprint(blueprint)
    assert sanitized_bp.url_prefix == '/test'
    assert sanitized_bp.version == 1
    assert sanitized_bp.strict_slashes is True

def test_sanitize_blueprint_no_version_no_strict_slashes(blueprint):
    blueprint_group = BlueprintGroup(url_prefix='/group')
    sanitized_bp = blueprint_group._sanitize_blueprint(blueprint)
    assert sanitized_bp.url_prefix == '/group/test'
    assert sanitized_bp.version is None
    assert sanitized_bp.strict_slashes is None
