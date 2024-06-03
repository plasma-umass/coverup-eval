# file sanic/blueprint_group.py:164-180
# lines []
# branches ['178->177']

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

def test_sanitize_blueprint_missing_attributes(blueprint_group, mock_blueprint):
    # Arrange
    mock_blueprint.url_prefix = None
    mock_blueprint.version = None
    mock_blueprint.strict_slashes = None

    group = blueprint_group(url_prefix="/api", version="1.0", strict_slashes=True)

    # Act
    sanitized_bp = group._sanitize_blueprint(mock_blueprint)

    # Assert
    assert sanitized_bp.url_prefix == "/api"
    assert sanitized_bp.version == "1.0"
    assert sanitized_bp.strict_slashes is True

def test_sanitize_blueprint_existing_attributes(blueprint_group, mock_blueprint):
    # Arrange
    mock_blueprint.url_prefix = "/v1"
    mock_blueprint.version = "2.0"
    mock_blueprint.strict_slashes = False

    group = blueprint_group(url_prefix="/api", version="1.0", strict_slashes=True)

    # Act
    sanitized_bp = group._sanitize_blueprint(mock_blueprint)

    # Assert
    assert sanitized_bp.url_prefix == "/api/v1"
    assert sanitized_bp.version == "2.0"
    assert sanitized_bp.strict_slashes is False
