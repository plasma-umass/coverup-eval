# file mimesis/providers/internet.py:265-274
# lines [265, 274]
# branches []

import pytest
from mimesis.providers.internet import Internet

# Assuming USER_AGENTS is a list of user agent strings.
USER_AGENTS = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    # Add more user agents if needed for the test
]

@pytest.fixture
def internet_provider(mocker):
    mocker.patch('mimesis.providers.internet.USER_AGENTS', USER_AGENTS)
    return Internet()

def test_user_agent(internet_provider):
    user_agent = internet_provider.user_agent()
    assert user_agent in USER_AGENTS
