# file sanic/blueprint_group.py:164-180
# lines [164, 172, 173, 174, 175, 176, 177, 178, 179, 180]
# branches ['172->173', '172->177', '177->178', '177->180', '178->177', '178->179']

import pytest
from unittest.mock import Mock
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

@pytest.fixture
def blueprint_group():
    class TestBlueprintGroup(BlueprintGroup):
        def __init__(self, url_prefix=None, version=None, strict_slashes=None):
            self._url_prefix = url_prefix
            self._version = version
            self._strict_slashes = strict_slashes
            self._blueprints = []

        @property
        def version(self):
            return self._version

        @version.setter
        def version(self, value):
            self._version = value

        @property
        def strict_slashes(self):
            return self._strict_slashes

        @strict_slashes.setter
        def strict_slashes(self, value):
            self._strict_slashes = value

        def __getitem__(self, index):
            return self._blueprints[index]

        def __setitem__(self, index, value):
            self._blueprints[index] = value

        def __delitem__(self, index):
            del self._blueprints[index]

        def __len__(self):
            return len(self._blueprints)

        def insert(self, index, value):
            self._blueprints.insert(index, value)

    return TestBlueprintGroup

def test_sanitize_blueprint(blueprint_group):
    bp_group = blueprint_group(url_prefix="/api", version="v1", strict_slashes=True)
    bp = Mock(spec=Blueprint)
    bp.url_prefix = None
    bp.version = None
    bp.strict_slashes = None

    sanitized_bp = bp_group._sanitize_blueprint(bp)

    assert sanitized_bp.url_prefix == "/api"
    assert sanitized_bp.version == "v1"
    assert sanitized_bp.strict_slashes is True

def test_sanitize_blueprint_with_existing_values(blueprint_group):
    bp_group = blueprint_group(url_prefix="/api", version="v1", strict_slashes=True)
    bp = Mock(spec=Blueprint)
    bp.url_prefix = "/v2"
    bp.version = "v2"
    bp.strict_slashes = False

    sanitized_bp = bp_group._sanitize_blueprint(bp)

    assert sanitized_bp.url_prefix == "/api/v2"
    assert sanitized_bp.version == "v2"
    assert sanitized_bp.strict_slashes is False
