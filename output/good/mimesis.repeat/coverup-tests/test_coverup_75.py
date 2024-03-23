# file mimesis/builtins/en.py:72-90
# lines [72, 82, 87, 88, 90]
# branches ['87->88', '87->90']

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.random import Random

@pytest.fixture
def usa_spec_provider():
    return USASpecProvider()

def test_personality_mbti(usa_spec_provider, mocker):
    mocker.patch.object(Random, 'choice', return_value='ISFJ')
    personality_type = usa_spec_provider.personality()
    assert personality_type == 'ISFJ'
    Random.choice.assert_called_once_with(('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                           'ISTP', 'ISFP', 'INFP', 'INTP',
                                           'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                           'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'))

def test_personality_rheti(usa_spec_provider, mocker):
    mocker.patch.object(Random, 'randint', return_value=5)
    personality_number = usa_spec_provider.personality(category='rheti')
    assert personality_number == 5
    Random.randint.assert_called_once_with(1, 10)
