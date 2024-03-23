# file mimesis/builtins/en.py:72-90
# lines [72, 82, 87, 88, 90]
# branches ['87->88', '87->90']

import pytest
from mimesis.builtins.en import USASpecProvider

def test_personality_with_rheti_category(mocker):
    # Mock the random methods to ensure consistent results
    mocker.patch('mimesis.random.Random.randint', return_value=5)
    mocker.patch('mimesis.random.Random.choice', return_value='ISFJ')

    provider = USASpecProvider()

    # Test the 'rheti' category
    rheti_personality = provider.personality(category='rheti')
    assert rheti_personality == 5, "Should return an integer between 1 and 10 for 'rheti' category"

    # Test the default 'mbti' category
    mbti_personality = provider.personality()
    assert mbti_personality == 'ISFJ', "Should return a string for 'mbti' category"

    # Test the default 'mbti' category with uppercase input
    mbti_personality_upper = provider.personality(category='MBTI')
    assert mbti_personality_upper == 'ISFJ', "Should return a string for 'mbti' category with uppercase input"

    # Cleanup is handled by pytest-mock through the mocker fixture
