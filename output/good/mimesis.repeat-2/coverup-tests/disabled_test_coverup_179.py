# file mimesis/providers/structure.py:102-138
# lines [112, 113, 116, 117, 122, 123, 124, 125, 133, 134, 136, 137]
# branches ['111->112', '115->116', '131->133', '133->134', '133->136']

import pytest
from mimesis.providers.structure import Structure
from mimesis.exceptions import NonEnumerableError

# Mock HTML_CONTAINER_TAGS for testing purposes
HTML_CONTAINER_TAGS = {
    'a': {'href': 'url', 'title': 'word'},
    'div': {'style': ['css']},
    'span': {'data-test': ['test1', 'test2']},
    'unsupported_tag': {'unsupported_attr': 'unsupported_value'}
}

@pytest.fixture
def structure_provider(mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    # Mock the css_property method to return a fixed value
    mocker.patch.object(Structure, 'css_property', return_value='css')
    # Mock the word method to return a fixed value
    mocker.patch('mimesis.providers.text.Text.word', return_value='word')
    # Mock the home_page method to return a fixed value
    mocker.patch('mimesis.providers.internet.Internet.home_page', return_value='http://example.com')
    return Structure()

def test_html_attribute_value(structure_provider):
    # Test with no tag and no attribute
    value = structure_provider.html_attribute_value()
    assert value in ['test1', 'test2', 'word', 'css', 'http://example.com']

    # Test with specified tag and no attribute
    value = structure_provider.html_attribute_value(tag='a')
    assert value in ['word', 'http://example.com']

    # Test with specified tag and specified attribute
    value = structure_provider.html_attribute_value(tag='div', attribute='style')
    assert value == 'css'

    # Test with specified tag and specified attribute with list of values
    value = structure_provider.html_attribute_value(tag='span', attribute='data-test')
    assert value in ['test1', 'test2']

    # Test with unsupported tag
    with pytest.raises(NotImplementedError):
        structure_provider.html_attribute_value(tag='unsupported_tag', attribute='href')

    # Test with unsupported attribute
    with pytest.raises(NotImplementedError):
        structure_provider.html_attribute_value(tag='a', attribute='unsupported_attr')

    # Test with unsupported value type
    with pytest.raises(NotImplementedError):
        structure_provider.html_attribute_value(tag='unsupported_tag', attribute='unsupported_attr')
