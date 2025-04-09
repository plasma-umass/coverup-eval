# file sanic/blueprint_group.py:73-80
# lines [73, 74, 80]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_url_prefix_property(self, mocker):
        # Create a mock instance of BlueprintGroup
        mock_instance = mocker.MagicMock(spec=BlueprintGroup)
        
        # Set the _url_prefix attribute
        mock_instance._url_prefix = "/test_prefix"
        
        # Access the url_prefix property
        result = BlueprintGroup.url_prefix.__get__(mock_instance)
        
        # Assert that the result is as expected
        assert result == "/test_prefix"
