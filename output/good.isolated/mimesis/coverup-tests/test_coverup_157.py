# file mimesis/providers/internet.py:161-169
# lines [169]
# branches []

import pytest
from mimesis.providers import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_emoji(internet_provider):
    emoji = internet_provider.emoji()
    assert isinstance(emoji, str) and emoji.startswith(':') and emoji.endswith(':')

def test_emoji_coverage(mocker):
    mock_random_choice = mocker.patch(
        'mimesis.random.Random.choice',
        return_value=':smile:'
    )
    internet = Internet()
    result = internet.emoji()
    assert result == ':smile:'
    mock_random_choice.assert_called_once()
