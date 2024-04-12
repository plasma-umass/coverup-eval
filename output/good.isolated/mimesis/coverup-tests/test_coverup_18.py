# file mimesis/providers/structure.py:74-100
# lines [74, 84, 85, 86, 88, 90, 91, 92, 93, 95, 96, 97, 98, 99]
# branches ['91->92', '91->95']

import pytest
from mimesis.providers import Structure
from mimesis.data import HTML_CONTAINER_TAGS

@pytest.fixture
def structure_provider():
    return Structure()

def test_html_tag_with_attributes(structure_provider):
    html = structure_provider.html()
    assert html.startswith('<') and html.endswith('>')
    tag_name = html.split(' ')[0][1:].split('>')[0].split('"')[0]
    assert tag_name in HTML_CONTAINER_TAGS
    assert any(attr in html for attr in HTML_CONTAINER_TAGS[tag_name])
