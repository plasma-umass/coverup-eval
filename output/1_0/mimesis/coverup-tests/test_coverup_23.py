# file mimesis/builtins/en.py:54-70
# lines [54, 62, 63, 64, 66, 67, 68, 69]
# branches ['63->64', '63->66']

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.random import Random

@pytest.fixture
def usa_spec_provider():
    return USASpecProvider()

def test_ssn_with_666_area(mocker, usa_spec_provider):
    # Mock randint to return 666 for the area code
    mocker.patch.object(Random, 'randint', side_effect=[666, 50, 1234])
    ssn = usa_spec_provider.ssn()
    assert ssn != '666-50-1234'
    assert ssn == '665-50-1234'

def test_ssn_with_non_666_area(mocker, usa_spec_provider):
    # Mock randint to return a non-666 area code
    mocker.patch.object(Random, 'randint', side_effect=[123, 50, 1234])
    ssn = usa_spec_provider.ssn()
    assert ssn == '123-50-1234'
