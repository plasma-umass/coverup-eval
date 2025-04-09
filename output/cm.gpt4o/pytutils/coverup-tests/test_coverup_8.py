# file pytutils/env.py:13-41
# lines [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41]
# branches ['27->exit', '27->28', '30->27', '30->31', '34->35', '34->37', '38->39', '38->41']

import pytest
import re
from collections import OrderedDict
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        "SINGLE_QUOTED='single_quoted_value'",
        'DOUBLE_QUOTED="double_quoted_value"',
        'ESCAPED_DOUBLE_QUOTED="escaped\\_double\\_quoted\\_value"'
    ]
    
    expected_output = OrderedDict([
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
        ('SINGLE_QUOTED', 'single_quoted_value'),
        ('DOUBLE_QUOTED', 'double_quoted_value'),
        ('ESCAPED_DOUBLE_QUOTED', 'escaped_double_quoted_value')
    ])
    
    result = OrderedDict(parse_env_file_contents(lines))
    
    assert result == expected_output

@pytest.fixture(autouse=True)
def clean_env(mocker):
    mocker.patch.dict('os.environ', {}, clear=True)
