# file sanic/blueprint_group.py:156-162
# lines [156, 162]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_len(self, mocker):
        # Mock the _blueprints attribute
        mock_blueprints = mocker.patch.object(BlueprintGroup, '_blueprints', new_callable=mocker.PropertyMock)
        mock_blueprints.return_value = [1, 2, 3]

        # Create an instance of BlueprintGroup
        blueprint_group = BlueprintGroup()

        # Assert the length is as expected
        assert len(blueprint_group) == 3
