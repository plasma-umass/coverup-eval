# file mimesis/builtins/ru.py:25-35
# lines [25, 30, 31, 32, 33, 35]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider(mocker):
    mock_data = {
        'sentence': {
            'head': ['Head1', 'Head2'],
            'p1': ['Part1_1', 'Part1_2'],
            'p2': ['Part2_1', 'Part2_2'],
            'tail': ['Tail1', 'Tail2']
        }
    }
    provider = RussiaSpecProvider()
    mocker.patch.object(provider, '_data', mock_data)
    return provider

def test_generate_sentence(russia_spec_provider):
    sentence = russia_spec_provider.generate_sentence()
    assert isinstance(sentence, str)
    assert len(sentence.split()) == 4
    mock_data = russia_spec_provider._data['sentence']
    assert all(part in mock_data[key] for part, key in zip(sentence.split(), ['head', 'p1', 'p2', 'tail']))
