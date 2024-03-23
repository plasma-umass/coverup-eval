# file mimesis/providers/structure.py:74-100
# lines [84, 85, 86, 88, 90, 91, 92, 93, 95, 96, 97, 98, 99]
# branches ['91->92', '91->95']

import pytest
from mimesis.providers import Structure
from mimesis.providers.text import Text
from unittest.mock import patch

@pytest.fixture
def structure_provider():
    return Structure()

def test_html_generation(structure_provider):
    with patch.object(Text, 'sentence', return_value='Test sentence.'):
        html = structure_provider.html()
        assert '<' in html and '>' in html
        assert 'Test sentence.' in html
        assert any(attr in html for attr in ['class', 'id', 'style', 'href', 'src'])
