# file mimesis/providers/structure.py:102-138
# lines [111, 112, 113, 115, 116, 117, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138]
# branches ['111->112', '111->115', '115->116', '115->120', '127->128', '127->129', '129->130', '129->131', '131->132', '131->133', '133->134', '133->136']

import pytest
from mimesis.providers.structure import Structure

HTML_CONTAINER_TAGS = {
    'div': {
        'class': ['container', 'row', 'col'],
        'id': 'word',
        'style': 'css',
        'data-url': 'url',
    },
    'span': {
        'class': ['highlight', 'note'],
        'id': 'word',
    },
}

@pytest.fixture
def structure():
    return Structure()

def test_html_attribute_value_no_tag_no_attribute(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure.random, 'choice', side_effect=lambda x: x[0])
    value = structure.html_attribute_value()
    assert value in ['container', 'highlight']

def test_html_attribute_value_with_tag_no_attribute(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure.random, 'choice', side_effect=lambda x: x[0])
    value = structure.html_attribute_value(tag='div')
    assert value in ['container', 'word', 'css', 'url']

def test_html_attribute_value_with_tag_and_attribute(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure.random, 'choice', side_effect=lambda x: x[0])
    value = structure.html_attribute_value(tag='div', attribute='class')
    assert value == 'container'

def test_html_attribute_value_with_unsupported_tag(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    with pytest.raises(NotImplementedError):
        structure.html_attribute_value(tag='unsupported', attribute='class')

def test_html_attribute_value_with_unsupported_attribute(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    with pytest.raises(NotImplementedError):
        structure.html_attribute_value(tag='div', attribute='unsupported')

def test_html_attribute_value_with_css_property(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure, 'css_property', return_value='color: red;')
    value = structure.html_attribute_value(tag='div', attribute='style')
    assert value == 'color: red;'

def test_html_attribute_value_with_word(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure, '_Structure__text', mocker.Mock(word=lambda: 'example'))
    value = structure.html_attribute_value(tag='div', attribute='id')
    assert value == 'example'

def test_html_attribute_value_with_url(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', HTML_CONTAINER_TAGS)
    mocker.patch.object(structure, '_Structure__inet', mocker.Mock(home_page=lambda: 'http://example.com'))
    value = structure.html_attribute_value(tag='div', attribute='data-url')
    assert value == 'http://example.com'

def test_html_attribute_value_with_unimplemented_type(structure, mocker):
    mocker.patch('mimesis.providers.structure.HTML_CONTAINER_TAGS', {'div': {'custom': 'unimplemented'}})
    with pytest.raises(NotImplementedError):
        structure.html_attribute_value(tag='div', attribute='custom')
