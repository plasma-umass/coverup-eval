# file semantic_release/hvcs.py:493-499
# lines [493, 499]
# branches []

import pytest
from semantic_release.hvcs import get_domain
from semantic_release import settings

# Mock HVCS class with a domain method
class MockHVCS:
    @staticmethod
    def domain():
        return "mockdomain.com"

# Test function to cover get_domain
def test_get_domain(mocker):
    # Mock the get_hvcs function to return an instance of MockHVCS
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=MockHVCS())
    
    # Call the function under test
    domain = get_domain()
    
    # Assert that the domain returned is correct
    assert domain == "mockdomain.com"
