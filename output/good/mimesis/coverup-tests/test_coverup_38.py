# file mimesis/builtins/en.py:72-90
# lines [72, 82, 87, 88, 90]
# branches ['87->88', '87->90']

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.providers.base import BaseProvider

@pytest.fixture()
def usa_spec_provider():
    return USASpecProvider()

def test_personality_mbti(usa_spec_provider):
    personality_type = usa_spec_provider.personality(category='mbti')
    assert personality_type in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                'ISTP', 'ISFP', 'INFP', 'INTP',
                                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

def test_personality_rheti(usa_spec_provider):
    personality_number = usa_spec_provider.personality(category='rheti')
    assert isinstance(personality_number, int)
    assert 1 <= personality_number <= 10

def test_personality_default(usa_spec_provider):
    personality_type = usa_spec_provider.personality()
    assert personality_type in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                'ISTP', 'ISFP', 'INFP', 'INTP',
                                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

def test_personality_unrecognized_category(usa_spec_provider):
    personality_type = usa_spec_provider.personality(category='unknown')
    assert personality_type in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                'ISTP', 'ISFP', 'INFP', 'INTP',
                                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
