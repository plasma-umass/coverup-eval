# file sanic/blueprint_group.py:59-71
# lines [59, 68, 69, 70, 71]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

def test_blueprint_group_initialization():
    url_prefix = "/api"
    version = "v1"
    strict_slashes = True

    blueprint_group = BlueprintGroup(url_prefix=url_prefix, version=version, strict_slashes=strict_slashes)

    assert blueprint_group._url_prefix == url_prefix
    assert blueprint_group._version == version
    assert blueprint_group._strict_slashes == strict_slashes
    assert blueprint_group._blueprints == []

def test_blueprint_group_default_initialization():
    blueprint_group = BlueprintGroup()

    assert blueprint_group._url_prefix is None
    assert blueprint_group._version is None
    assert blueprint_group._strict_slashes is None
    assert blueprint_group._blueprints == []
