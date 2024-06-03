# file mimesis/builtins/en.py:54-70
# lines [54, 62, 63, 64, 66, 67, 68, 69]
# branches ['63->64', '63->66']

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.providers.base import BaseProvider

@pytest.fixture
def usa_spec_provider():
    return USASpecProvider(seed=0)

def test_ssn(usa_spec_provider, mocker):
    mock_random = mocker.patch.object(usa_spec_provider, 'random')
    
    # Test case where area is 666 and should be changed to 665
    mock_random.randint.side_effect = [666, 50, 1234]
    ssn = usa_spec_provider.ssn()
    assert ssn == '665-50-1234'
    
    # Test case where area is not 666
    mock_random.randint.side_effect = [123, 50, 1234]
    ssn = usa_spec_provider.ssn()
    assert ssn == '123-50-1234'
