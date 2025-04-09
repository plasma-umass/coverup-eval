# file mimesis/providers/text.py:124-133
# lines [124, 132, 133]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_color(text_provider, mocker):
    # Mock the _data attribute to ensure the test is isolated
    mocker.patch.object(text_provider, '_data', {'color': ['Red', 'Green', 'Blue']})
    
    # Call the color method
    color_name = text_provider.color()
    
    # Assert that the returned color name is in the mocked color list
    assert color_name in ['Red', 'Green', 'Blue']
