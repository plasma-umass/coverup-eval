# file pytutils/env.py:13-41
# lines []
# branches ['30->27']

import pytest
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents_branch_coverage():
    lines = [
        "TEST='single_quotes'",
        'THISIS="double_quotes"',
        'YOLO=no_quotes',
        'INVALID LINE'
    ]
    
    result = list(parse_env_file_contents(lines))
    
    assert result == [
        ('TEST', 'single_quotes'),
        ('THISIS', 'double_quotes'),
        ('YOLO', 'no_quotes')
    ]
