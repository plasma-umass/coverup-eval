# file mimesis/providers/structure.py:74-100
# lines [74, 84, 85, 86, 88, 90, 91, 92, 93, 95, 96, 97, 98, 99]
# branches ['91->92', '91->95']

import pytest
from mimesis.providers import Structure
from mimesis.providers.text import Text
from unittest.mock import Mock

@pytest.fixture
def structure_provider():
    provider = Structure()
    provider.random = Mock()
    provider.__text = Text()
    return provider

def test_html(structure_provider):
    # Mocking the random.choice to return a specific tag
    structure_provider.random.choice.return_value = 'div'
    # Mocking the random.randint to return a specific number of attributes
    structure_provider.random.randint.return_value = 1
    # Mocking the random.sample to return a specific attribute
    structure_provider.random.sample.return_value = ['class']
    # Mocking the html_attribute_value to return a specific value
    structure_provider.html_attribute_value = Mock(return_value='example-class')

    # Generate the HTML
    html = structure_provider.html()

    # Assertions to check if the HTML is generated correctly
    assert '<div class="example-class">' in html
    assert '</div>' in html
    assert 'example-class' in html

    # Clean up mocks
    structure_provider.random.choice.reset_mock()
    structure_provider.random.randint.reset_mock()
    structure_provider.random.sample.reset_mock()
    structure_provider.html_attribute_value.reset_mock()
