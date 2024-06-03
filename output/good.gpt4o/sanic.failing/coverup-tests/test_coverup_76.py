# file sanic/blueprint_group.py:73-80
# lines [73, 74, 80]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_url_prefix_property(self, mocker):
        # Create a mock instance of BlueprintGroup
        mock_blueprint_group = mocker.MagicMock(spec=BlueprintGroup)
        
        # Set the _url_prefix attribute
        mock_blueprint_group._url_prefix = "/test_prefix"
        
        # Access the url_prefix property
        url_prefix = BlueprintGroup.url_prefix.__get__(mock_blueprint_group)
        
        # Assert that the url_prefix property returns the correct value
        assert url_prefix == "/test_prefix"
