# file mimesis/providers/structure.py:74-100
# lines [74, 84, 85, 86, 88, 90, 91, 92, 93, 95, 96, 97, 98, 99]
# branches ['91->92', '91->95']

import pytest
from mimesis.providers.structure import Structure
from mimesis import Generic

@pytest.fixture
def structure():
    generic = Generic()
    return generic.structure

def test_html(structure, mocker):
    # Mocking the random choice to ensure a specific tag is chosen
    mocker.patch.object(structure.random, 'choice', return_value='span')
    # Mocking the random sample to ensure specific attributes are chosen
    mocker.patch.object(structure.random, 'sample', return_value=['class', 'id'])
    # Mocking the random sentence generation
    mocker.patch.object(structure._Structure__text, 'sentence', return_value='Test sentence.')
    # Mocking the html_attribute_value to return specific values for attributes
    mocker.patch.object(structure, 'html_attribute_value', side_effect=lambda tag, attr: attr)

    result = structure.html()
    
    assert result == '<span class="class" id="id">Test sentence.</span>'

    # Clean up mocks
    mocker.stopall()
