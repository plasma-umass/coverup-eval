# file cookiecutter/prompt.py:44-78
# lines [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78]
# branches ['54->55', '54->57', '57->58', '57->60']

import pytest
from click.testing import CliRunner
from collections import OrderedDict
from cookiecutter.prompt import read_user_choice

def test_read_user_choice(mocker):
    mocker.patch('click.prompt', return_value='1')
    options = ['option1', 'option2']
    result = read_user_choice('test_var', options)
    assert result == 'option1'

    mocker.patch('click.prompt', return_value='2')
    result = read_user_choice('test_var', options)
    assert result == 'option2'

    with pytest.raises(TypeError):
        read_user_choice('test_var', 'not-a-list')

    with pytest.raises(ValueError):
        read_user_choice('test_var', [])
