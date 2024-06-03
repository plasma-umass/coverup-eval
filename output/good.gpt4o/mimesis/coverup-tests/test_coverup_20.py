# file mimesis/providers/structure.py:53-72
# lines [53, 61, 62, 64, 65, 66, 67, 68, 69, 70, 72]
# branches ['64->65', '64->66', '66->67', '66->68', '68->69', '68->72']

import pytest
from mimesis.providers.structure import Structure
from mimesis.data import CSS_PROPERTIES, CSS_SIZE_UNITS
from mimesis import Text

@pytest.fixture
def structure_provider(mocker):
    provider = Structure()
    mocker.patch.object(provider, '_Structure__text', Text())
    return provider

def test_css_property_color(structure_provider, mocker):
    mocker.patch('mimesis.providers.structure.CSS_PROPERTIES', {'color': 'color'})
    result = structure_provider.css_property()
    assert result.startswith('color: #')

def test_css_property_size(structure_provider, mocker):
    mocker.patch('mimesis.providers.structure.CSS_PROPERTIES', {'width': 'size'})
    result = structure_provider.css_property()
    assert result.startswith('width: ')
    assert any(result.endswith(unit) for unit in CSS_SIZE_UNITS)

def test_css_property_list(structure_provider, mocker):
    mocker.patch('mimesis.providers.structure.CSS_PROPERTIES', {'display': ['block', 'inline', 'none']})
    result = structure_provider.css_property()
    assert result.startswith('display: ')
    assert result.split(': ')[1] in ['block', 'inline', 'none']
