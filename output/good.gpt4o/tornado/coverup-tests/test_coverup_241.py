# file tornado/options.py:160-161
# lines [161]
# branches []

import pytest
from tornado.options import OptionParser, _Option

def test_option_parser_iteration(mocker):
    # Create a mock _Option object
    mock_option1 = mocker.Mock(spec=_Option)
    mock_option2 = mocker.Mock(spec=_Option)
    mock_option1.name = 'option1'
    mock_option2.name = 'option2'

    # Mock the _options attribute to simulate the internal state
    mock_options = {
        'opt1': mock_option1,
        'opt2': mock_option2
    }

    parser = OptionParser()
    # Directly set the _options attribute using the internal dictionary
    parser.__dict__['_options'] = mock_options

    # Collect the names using the __iter__ method
    option_names = list(parser)

    # Assert that the names are as expected
    assert option_names == ['option1', 'option2']
