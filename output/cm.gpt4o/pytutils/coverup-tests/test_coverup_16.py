# file pytutils/env.py:7-10
# lines [7, 8, 9, 10]
# branches []

import os
import pytest
from pytutils.env import expand

def test_expand_with_env_var(mocker):
    mocker.patch.dict(os.environ, {"TEST_VAR": "test_value"})
    result = expand("$TEST_VAR")
    assert result == "test_value"

def test_expand_with_user_home(mocker):
    mocker.patch("os.path.expanduser", return_value="/mocked/home/user")
    result = expand("~")
    assert result == "/mocked/home/user"

def test_expand_with_both(mocker):
    mocker.patch.dict(os.environ, {"TEST_VAR": "test_value"})
    mocker.patch("os.path.expanduser", side_effect=lambda x: x.replace("~", "/mocked/home/user"))
    result = expand("~/$TEST_VAR")
    assert result == "/mocked/home/user/test_value"
