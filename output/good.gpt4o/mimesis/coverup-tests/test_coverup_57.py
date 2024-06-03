# file mimesis/builtins/en.py:72-90
# lines [72, 82, 87, 88, 90]
# branches ['87->88', '87->90']

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.providers.base import BaseProvider

class MockRandom:
    def randint(self, a, b):
        return 5

    def choice(self, seq):
        return seq[0]

@pytest.fixture
def usa_spec_provider(mocker):
    provider_instance = USASpecProvider()
    mocker.patch.object(provider_instance, 'random', new_callable=lambda: MockRandom())
    return provider_instance

def test_personality_mbtis(usa_spec_provider):
    result = usa_spec_provider.personality('mbti')
    assert result in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                      'ISTP', 'ISFP', 'INFP', 'INTP',
                      'ESTP', 'ESFP', 'ENFP', 'ENTP',
                      'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

def test_personality_rheti(usa_spec_provider):
    result = usa_spec_provider.personality('rheti')
    assert result == 5
