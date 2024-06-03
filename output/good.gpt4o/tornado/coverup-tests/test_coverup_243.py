# file tornado/options.py:700-707
# lines [707]
# branches []

import pytest
from tornado.options import OptionParser, options

@pytest.fixture
def reset_options():
    # Save the current state of options
    saved_options = options._options.copy()
    saved_values = {name: opt.value() for name, opt in options._options.items()}
    yield
    # Restore the original state of options
    options._options.clear()
    options._options.update(saved_options)
    for name, value in saved_values.items():
        options._options[name].set(value)

def test_parse_command_line_executes_line_707(reset_options, mocker):
    mocker.patch.object(OptionParser, 'parse_command_line', return_value=['--example'])
    
    from tornado.options import parse_command_line
    
    result = parse_command_line(['--example'])
    
    assert result == ['--example']
    OptionParser.parse_command_line.assert_called_once_with(['--example'], final=True)
