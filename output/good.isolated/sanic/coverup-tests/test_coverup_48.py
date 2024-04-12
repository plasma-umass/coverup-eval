# file sanic/blueprint_group.py:73-80
# lines [73, 74, 80]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    bg = BlueprintGroup()
    bg._url_prefix = '/test_prefix'
    yield bg
    bg._url_prefix = None

def test_url_prefix(blueprint_group):
    assert blueprint_group.url_prefix == '/test_prefix'
