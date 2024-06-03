# file mimesis/providers/internet.py:265-274
# lines [265, 274]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_user_agent(mocker):
    # Mock the USER_AGENTS list to ensure the test is deterministic
    mock_user_agents = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    ]
    mocker.patch('mimesis.providers.internet.USER_AGENTS', mock_user_agents)
    
    internet = Internet()
    user_agent = internet.user_agent()
    
    # Assert that the returned user agent is one of the mocked user agents
    assert user_agent in mock_user_agents
