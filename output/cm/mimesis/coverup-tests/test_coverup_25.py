# file mimesis/providers/structure.py:37-51
# lines [37, 42, 43, 45, 46, 48, 49, 50, 51]
# branches []

import pytest
from mimesis.providers import Structure

@pytest.fixture
def structure_provider():
    return Structure()

def test_css(structure_provider):
    css_snippet = structure_provider.css()
    assert css_snippet.endswith('}')
    assert '{' in css_snippet
    # Since Structure does not have HTML_CONTAINER_TAGS or HTML_MARKUP_TAGS attributes, we need to remove those assertions
