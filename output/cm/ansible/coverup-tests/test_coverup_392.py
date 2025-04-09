# file lib/ansible/utils/context_objects.py:63-82
# lines [63, 64, 74, 75, 76, 77, 78, 80, 81, 82]
# branches ['76->77', '76->78']

import pytest
from ansible.utils.context_objects import CLIArgs

def _make_immutable(value):
    # Mocking the _make_immutable function for the purpose of this test
    if isinstance(value, list):
        return tuple(value)
    return value

@pytest.fixture
def mock_make_immutable(mocker):
    return mocker.patch('ansible.utils.context_objects._make_immutable', side_effect=_make_immutable)

class OptionsMock:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

@pytest.fixture
def options_mock():
    return OptionsMock(arg1='value1', arg2=[1, 2, 3])

class TestCLIArgs:
    def test_cliargs_init_and_from_options(self, mock_make_immutable, options_mock):
        # Test the from_options class method
        cli_args = CLIArgs.from_options(options_mock)
        assert isinstance(cli_args, CLIArgs)
        assert cli_args['arg1'] == 'value1'
        assert cli_args['arg2'] == (1, 2, 3)  # _make_immutable should have converted list to tuple

        # Test the __init__ method directly
        direct_cli_args = CLIArgs({'arg1': 'value1', 'arg2': [1, 2, 3]})
        assert isinstance(direct_cli_args, CLIArgs)
        assert direct_cli_args['arg1'] == 'value1'
        assert direct_cli_args['arg2'] == (1, 2, 3)  # _make_immutable should have converted list to tuple

        # Ensure that the _make_immutable function was called the correct number of times
        assert mock_make_immutable.call_count == 4
