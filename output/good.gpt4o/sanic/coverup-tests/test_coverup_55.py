# file sanic/blueprint_group.py:164-180
# lines [164, 172, 173, 174, 175, 176, 177, 178, 179, 180]
# branches ['172->173', '172->177', '177->178', '177->180', '178->177', '178->179']

import pytest
from unittest.mock import Mock
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

@pytest.fixture
def mock_blueprint():
    return Mock(spec=Blueprint)

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

        @property
        def strict_slashes(self):
            return self._strict_slashes

        def __len__(self):
            return len(self._blueprints)

        def __getitem__(self, index):
            return self._blueprints[index]

        def __setitem__(self, index, value):
            self._blueprints[index] = value

        def __delitem__(self, index):
            del self._blueprints[index]

        def insert(self, index, value):
            self._blueprints.insert(index, value)

    return TestBlueprintGroup

def test_sanitize_blueprint(blueprint_group, mock_blueprint):
    # Test case where url_prefix is set
    group = blueprint_group(url_prefix="/api", version="1.0", strict_slashes=True)
    mock_blueprint.url_prefix = "/v1"
    mock_blueprint.version = None
    mock_blueprint.strict_slashes = None

    sanitized_bp = group._sanitize_blueprint(mock_blueprint)

    assert sanitized_bp.url_prefix == "/api/v1"
    assert sanitized_bp.version == "1.0"
    assert sanitized_bp.strict_slashes is True

    # Test case where url_prefix is not set
    group = blueprint_group(version="2.0", strict_slashes=False)
    mock_blueprint.url_prefix = None
    mock_blueprint.version = None
    mock_blueprint.strict_slashes = None

    sanitized_bp = group._sanitize_blueprint(mock_blueprint)

    assert sanitized_bp.url_prefix is None
    assert sanitized_bp.version == "2.0"
    assert sanitized_bp.strict_slashes is False
