# file sanic/blueprint_group.py:130-141
# lines [130, 141]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class MockBlueprint:
    def __init__(self):
        self.url_prefix = None
        self.version = None
        self.strict_slashes = None

@pytest.fixture
def blueprint_group():
    bg = BlueprintGroup()
    yield bg
    bg.clear()

def test_blueprint_group_setitem(blueprint_group):
    blueprint1 = MockBlueprint()
    blueprint2 = MockBlueprint()
    blueprint_group.append(blueprint1)
    
    assert blueprint_group[0] == blueprint1, "Initial set item failed"
    
    blueprint_group[0] = blueprint2
    assert blueprint_group[0] == blueprint2, "Set item did not replace the existing blueprint"
