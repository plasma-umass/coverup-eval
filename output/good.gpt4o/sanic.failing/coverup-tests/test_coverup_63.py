# file sanic/blueprint_group.py:110-114
# lines [110, 114]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_iter(self, mocker):
        # Mock the _blueprints attribute
        mock_blueprints = mocker.patch.object(BlueprintGroup, '_blueprints', new_callable=mocker.PropertyMock)
        mock_blueprints.return_value = ['blueprint1', 'blueprint2', 'blueprint3']
        
        # Create an instance of BlueprintGroup
        blueprint_group = BlueprintGroup()
        
        # Test the __iter__ method
        iterator = iter(blueprint_group)
        assert list(iterator) == ['blueprint1', 'blueprint2', 'blueprint3']
