# file thonny/roughparse.py:752-756
# lines [754, 755, 756]
# branches []

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser_fixture(mocker):
    # Mocking the HyperParser object
    mocker.patch.object(HyperParser, '__init__', lambda self: None)
    hp = HyperParser()
    hp.isopener = {}
    hp.indexbracket = 0
    hp.rawtext = ""
    hp.bracketing = {}
    return hp

def test_is_in_code_executes_missing_lines(hyperparser_fixture):
    # Set up the HyperParser object to hit the missing lines
    hyperparser_fixture.isopener = {0: False}
    hyperparser_fixture.rawtext = "# Some comment"
    hyperparser_fixture.bracketing = {0: (0, None)}
    
    # Call the method under test
    result = hyperparser_fixture.is_in_code()
    
    # Assert that the result is True, as the index is not an opener and the rawtext does not start with a quote
    assert result == True

    # Change the conditions to hit the other branch
    hyperparser_fixture.isopener = {0: True}
    hyperparser_fixture.rawtext = '"A string"'
    hyperparser_fixture.bracketing = {0: (0, None)}
    
    # Call the method under test
    result = hyperparser_fixture.is_in_code()
    
    # Assert that the result is False, as the index is an opener and the rawtext starts with a quote
    assert result == False
